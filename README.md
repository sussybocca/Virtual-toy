# 🎮 Virtually — Virtual Toy Environment 0.56  
### Build, Customize, and Run Fully Simulated Virtual Environments

**Virtually** is a Python-powered virtual OS simulator that lets you build miniature operating systems using simple folders.  
Design a full environment using plain files — no ISO, no VM, no CPU virtualization.

Create:

- Boot screen  
- Desktop animation  
- Program folder  
- File system  
- Environment metadata  

And launch it inside a **full-screen simulated virtual machine window**.

---

# 📁 Virtual Environment Structure (IMPORTANT)

To create a virtual environment, the user must follow this exact folder layout:
MyVirtualEnvironment/
│
├── Boot/                       # Boot folder (BUP)
│   └── Boot.txt                # Boot screen text or boot script
│
├── Desktop/                    # Desktop animation folder
│   └── Desktop.mp4             # MP4 animation (looped background)
│
├── ProgramFiles/               # Program folder (VTP)
│   ├── App1/
│   │   └── main.vtpapp         # Example program file
│   ├── App2/
│   └── …
│
├── System/                     # System folder (VTF/System)
│   ├── config.sys              # System configuration
│   ├── runtime/                # System resources
│   └── …
│
└── env.json                    # Auto-generated environment metadata
---

## 📌 Required Storage Locations (Where to Put Your Virtual Environment)

Virtually supports **three types of environment locations**:

---

### 🖥️ 1. Desktop Storage  
You may place your environment directly on your desktop:
C:/Users/YOURNAME/Desktop/MyVirtualEnvironment/
Virtually will automatically detect it when you browse to the folder.

---

### 📦 2. Local Program Storage  
Virtually also supports a local "Programs" directory for more organized environments:
C:/Users/YOURNAME/Programs/VirtuallyEnvs/MyVirtualEnvironment/
This is recommended if you plan on storing multiple virtual environments.

---

### 💾 3. USB Storage (FAT32 Required)

Virtually supports running virtual environments from a **USB drive**, but the USB **must be formatted as FAT32**.

Example USB path:
E:/VirtualEnvironments/MyVirtualEnvironment/
**Why FAT32?**

- Ensures cross-device compatibility  
- Prevents long-file-path issues  
- Allows Virtually to read boot, system, and program files without permission restrictions  

If the USB drive is NOT FAT32, Virtually will display:
ERROR: USB device must be formatted as FAT32.
---

## ✔️ Minimum Required Environment Files
