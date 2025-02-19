# IP-GeoTracker
# IP Tracker Tool 🌍

A simple IP tracking tool that fetches **geolocation and ISP details** using the **IP2Location.io API**.  
It provides **colorful output**, **ISP details**, **proxy/VPN/TOR detection**, and **Google Maps location links**.  

## 🔥 Features
✅ Fetches **Country, City, ISP, and ASN**  
✅ Detects **Wi-Fi vs Mobile Data connections**  
✅ Checks for **VPN, Proxy, and TOR usage**  
✅ Generates **Google Maps link for IP location**  
✅ Simple **text-based** output with colors  

---

## 📥 Installation
1️⃣ **Clone the repository**  
```bash
git clone https://github.com/yourusername/IP-Tracker-Tool.git
cd IP-Tracker-Tool

2️⃣ Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Get an API Key from IP2Location.io

4️⃣ Edit ip_tracker.py and replace:

python
Copy
Edit
API_KEY = "your_api_key_here"
5️⃣ Run the tool

bash
Copy
Edit
python ip_tracker.py
🔍 Example Output
yaml
Copy
Edit
--- IP Information ---
IP Address:            8.8.8.8
Country:               United States
Region:                California
City:                  Mountain View
Latitude:              37.405
Longitude:             -122.078
ISP:                   Google LLC
ISP Domain:            google.com
ASN (Autonomous System Number): AS15169
Connection Type:       Wi-Fi/Ethernet
Proxy:                 No
VPN:                   No
TOR:                   No

Google Maps Location: https://www.google.com/maps?q=37.405,-122.078
