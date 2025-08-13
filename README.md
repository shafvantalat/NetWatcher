# 🖥️ NetWatcher

NetWatcher is a simple yet powerful Python tool to monitor all devices connected to your local network.  
It displays the IP address, MAC address, and vendor details of each connected device in real time.

---

## 🚀 Features
- Scans your local network for connected devices
- Retrieves MAC addresses and vendor information
- Automatically updates the MAC vendor database
- Displays results in a clean, tabular format

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/shafvantalat/NetWatcher.git
cd NetWatcher
```

### 2. Create a virtual environment
```bash
python -m venv venv
```
### 3. Activate the virtual environment

In Windows (CMD)
```
venv\Scripts\activate
```

Windows (Git Bash)
```bash
source venv/Scripts/activate
```

Linux/Mac
```
source venv/bin/activate
```

### 4. Install dependencies
```
pip install -r requirements.txt
```

▶️ Usage
### 5. Run the script in administrator privileges:

#### If you are using VS Code, save all files and close the application.

#### Then, right-click on the Visual Studio Code icon and select “Run as Administrator”.

#### Alternatively, you can open Command Prompt or your terminal with administrator privileges and run the script from there.

```
python netwatcher.py
```
Example output:

[INFO] Updating MAC vendor database...

[INFO] Vendor database updated successfully.

Current Devices (3 total) at 20:41:49:

IP Address         MAC Address        Vendor

------------------------------------------------------------

192.168.xxx.xx    ff:ff:ff:ff:ff:ff  ASUSTeK Computer Inc.

192.168.xxx.xx    ff:ff:ff:ff:ff:ff  Samsung Electronics Co.,Ltd

192.168.xxx.xx    ff:ff:ff:ff:ff:ff  AzureWave Technology Inc.


## ⚠️ Fix for Windows Users — Npcap Installation 
### If you see:

WARNING: No libpcap provider available ! pcap won't be used

You need to install Npcap for full packet capturing support.

### Download Npcap from: https://nmap.org/npcap/

### During installation, check:

#### ✅ "Install Npcap in WinPcap API-compatible mode"

#### ✅ "Start Npcap driver at boot time"

#### ✅ Restart your computer.

### 📂 Requirements
#### Python 3.8+
#### scapy, mac-vendor-lookup, colorama

You can install them all via:
```bash
pip install -r requirements.txt
```

## 📜 License
### This project is licensed under the MIT License.


# 👤 Author

## Muhammed Shafvan

### GitHub: https://github.com/shafvantalat

### Portfolio: https://shafvan.netlify.app

### Instagram: https://instagram.com/shafvantalat_

### Email: muhammedshafvan269@gmail.com

---

####  So far this program tested on only on Windows 11.

#### send me Reviews through Email or Instagram
