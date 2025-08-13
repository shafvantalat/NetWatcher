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

1. **Clone the repository**
```bash
git clone https://github.com/shafvantalat/NetWatcher.git
cd NetWatcher
Create a virtual environment

bash
Copy
Edit
python -m venv venv
Activate the virtual environment

Windows (CMD)

bash
Copy
Edit
venv\Scripts\activate
Windows (Git Bash)

bash
Copy
Edit
source venv/Scripts/activate
Linux/Mac

bash
Copy
Edit
source venv/bin/activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
▶️ Usage
Run the script:

bash
Copy
Edit
python netwatcher.py
Example output:

less
Copy
Edit
[INFO] Updating MAC vendor database...
[INFO] Vendor database updated successfully.

Current Devices (3 total) at 20:41:49:
IP Address         MAC Address        Vendor
------------------------------------------------------------
192.168.229.89     16:fe:c6:2f:22:04  Unknown Vendor
192.168.229.120    e8:aa:cb:23:c6:32  Samsung Electronics Co.,Ltd
192.168.229.181    f8:3d:c6:6e:0d:3f  AzureWave Technology Inc.
📂 Requirements
Python 3.8+

scapy

mac-vendor-lookup

requests

tabulate

You can install them all via:

bash
Copy
Edit
pip install -r requirements.txt
📜 License
This project is licensed under the MIT License.

👤 Author
Muhammed Shafvan

GitHub: shafvantalat

Portfolio: muhammed-shafvan.vercel.app

Email: muhammedshafvan269@gmail.com

yaml
Copy
Edit

---

If you want, I can **also add an "Updating Devices in Real-Time" section** so people know they can loop it for live monitoring.  
Do you want me to include that?








Ask ChatGPT
