from PyQt5 import QtWidgets, QtGui, QtCore, QtMultimedia, QtMultimediaWidgets
import os
import subprocess
from virtual_toy.utils import run_program, save_log

class VirtualMachineWindow(QtWidgets.QMainWindow):
    def __init__(self, vm_folder, desktop_animation=None):
        super().__init__()
        self.vm_folder = vm_folder
        self.desktop_animation = desktop_animation
        self.programs_folder = os.path.join(vm_folder, "Programs")
        self.filesystem_folder = os.path.join(vm_folder, "System")
        self.boot_folder = os.path.join(vm_folder, "Boot")

        self.setWindowTitle("Virtual Machine - Full Screen")
        self.showFullScreen()

        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QtWidgets.QVBoxLayout(self.central_widget)

        # Boot screen
        self.boot_label = QtWidgets.QLabel()
        self.boot_label.setAlignment(QtCore.Qt.AlignCenter)
        self.main_layout.addWidget(self.boot_label)
        self.show_boot_screen()

        # Desktop area
        self.desktop_widget = QtWidgets.QWidget()
        self.desktop_layout = QtWidgets.QGridLayout(self.desktop_widget)
        self.main_layout.addWidget(self.desktop_widget)

        # Media Player for desktop animation
        self.media_player = QtMultimedia.QMediaPlayer(None, QtMultimedia.QMediaPlayer.VideoSurface)
        self.video_widget = QtMultimediaWidgets.QVideoWidget()
        self.desktop_layout.addWidget(self.video_widget, 0, 0, 1, 4)
        self.media_player.setVideoOutput(self.video_widget)

        if self.desktop_animation and os.path.exists(self.desktop_animation):
            self.play_desktop_animation(self.desktop_animation)

        # Load programs as clickable buttons
        self.load_program_icons()

        # File system viewer
        self.fs_view = QtWidgets.QTreeView()
        self.fs_model = QtWidgets.QFileSystemModel()
        self.fs_model.setRootPath(self.filesystem_folder)
        self.fs_view.setModel(self.fs_model)
        self.fs_view.setRootIndex(self.fs_model.index(self.filesystem_folder))
        self.fs_view.setColumnWidth(0, 300)
        self.desktop_layout.addWidget(self.fs_view, 1, 0, 1, 4)

    # ------------------ Boot Screen ------------------ #
    def show_boot_screen(self):
        boot_txt = os.path.join(self.boot_folder, "Boot.txt")
        if os.path.exists(boot_txt):
            with open(boot_txt, "r") as f:
                text = f.read()
            self.boot_label.setText(f"<pre>{text}</pre>")
            save_log(f"Boot screen loaded from {boot_txt}")
        else:
            self.boot_label.setText("Boot screen missing!")
            save_log("Boot.txt not found in VM")

    # ------------------ Desktop Animation ------------------ #
    def play_desktop_animation(self, mp4_path):
        url = QtCore.QUrl.fromLocalFile(mp4_path)
        media_content = QtMultimedia.QMediaContent(url)
        self.media_player.setMedia(media_content)
        self.media_player.setVolume(50)
        self.media_player.play()
        save_log(f"Playing desktop animation: {mp4_path}")

    # ------------------ Programs ------------------ #
    def load_program_icons(self):
        if not os.path.exists(self.programs_folder):
            return
        row = 0
        col = 0
        for file in os.listdir(self.programs_folder):
            file_path = os.path.join(self.programs_folder, file)
            btn = QtWidgets.QPushButton(file)
            btn.setFixedSize(120, 40)
            btn.clicked.connect(lambda checked, fp=file_path: run_program(fp))
            self.desktop_layout.addWidget(btn, row + 1, col)
            col += 1
            if col > 3:
                col = 0
                row += 1
