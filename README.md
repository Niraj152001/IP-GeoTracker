# IP Tracker Tool 🌍

**IP-Tracker-Tool** is a powerful command-line tool that retrieves **geolocation, ISP details, and security information** about any IP address using the [IP2Location.io](https://www.ip2location.io/) API. It is useful for **OSINT investigations, cybersecurity analysis, and network diagnostics.**

## 🚀 Features
- ✅ **Geolocation Data** – Country, City, Region, Latitude, Longitude
- ✅ **ISP Details** – ISP Name, ASN, Domain
- ✅ **Network Type** – Wi-Fi or Mobile Data Detection
- ✅ **Security Check** – Detects VPN, Proxy, and TOR usage
- ✅ **Google Maps Link** – Clickable link for easy location viewing
- ✅ **Colorful CLI Output** – Enhanced readability with colored text

---

## 🛠️ Installation
### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/IP-Tracker-Tool.git
cd IP-Tracker-Tool
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Run the Tool**
```bash
python ip_tracker.py
```

---

## 📌 Usage
1. Enter an IP address when prompted.
2. The tool fetches and displays geolocation, ISP, and security details.
3. If coordinates are available, a **Google Maps link** is generated for easy viewing.

### **Example Output:**
```
🔍 IP Address: 192.168.1.1
🌍 Location: New York, United States
📡 ISP: Example ISP (ASN: 12345)
🔎 Network Type: Wi-Fi
🛡️ Security: No VPN/Proxy detected
📍 Google Maps: https://www.google.com/maps?q=40.7128,-74.0060
```

---

## 📌 API Key Setup
1. **Get an API key** from [IP2Location.io](https://www.ip2location.io/).
2. **Edit the script** and replace `YOUR_API_KEY` with your actual API key.

---

## 📜 License
This project is **open-source** under the MIT License.

---

## 🤝 Contributions
Feel free to submit **issues, pull requests, or suggestions** to improve this tool!

### **Author:** Neeraj Kumar 

---

🚀 **Happy Tracking!**

