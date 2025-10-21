🕵️‍♂️ Network Reconnaissance Tool

A simple **Network Reconnaissance Tool** built in **Python** that automates common information-gathering techniques such as:
- **Port scanning** using `nmap`
- **WHOIS lookups**
- **DNS enumeration**
- **Timestamped scanning reports**

This tool is designed for educational and ethical security testing within authorized environments only.

---

## 🚀 Features

✅ Perform detailed Nmap scans (custom port ranges)  
✅ Gather WHOIS information about a target domain/IP  
✅ Enumerate DNS records (A, MX, NS, etc.)  
✅ Automatically save results with scan timestamps  
✅ Simple command-line interface  

---

## 🧰 Requirements

Before running, make sure you have:

- **Python 3.8+**
- **Nmap** installed (`sudo apt install nmap`)
- **Required Python libraries:**
  ```bash
  pip install python-nmap python-whois dnspython

## ⚙️ Installation

Clone the repository

git clone git@github.com:AnisBengaji/network-recon-tool.git
cd network-recon-tool


(Optional) Create a virtual environment

python3 -m venv venv
source venv/bin/activate


Install dependencies

pip install -r requirements.txt


## Usage

Run the tool from the terminal:
sudo venv/bin/python3 src/main.py [TARGET] [OPTIONS] 


🧠 Notes

Always run this tool only on networks or systems you own or have explicit permission to test.

Unauthorized scanning can be illegal — use responsibly.
