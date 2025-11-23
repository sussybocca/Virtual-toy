import os

def validate_program_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
    for file in os.listdir(path):
        if not file.endswith((".py", ".js", ".cs")):
            raise ValueError(f"Invalid file type in program folder: {file}")

def validate_filesystem(path):
    system_path = os.path.join(path, "System")
    if not os.path.exists(system_path):
        os.makedirs(system_path)
    for file in os.listdir(system_path):
        if not file.endswith((".js", ".html")):
            raise ValueError(f"Invalid file type in file system: {file}")
