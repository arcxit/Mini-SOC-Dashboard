# Mini SOC Dashboard (SIEM Log Monitor)

A lightweight SOC dashboard that parses Linux `auth.log` files to detect brute-force login attempts and suspicious IPs.  
Provides a simple Flask-based dashboard for real-time monitoring and incident triage.

---

## 🚀 Features
- Parses authentication logs to flag failed login attempts
- Detects brute-force patterns and suspicious IPs
- Displays alerts on a clean web dashboard
- Helps in **Root Cause Identification** and **Incident Management**

---

## ⚙️ Setup
```bash
git clone https://github.com/arcxit/Mini-SOC-Dashboard.git
cd Mini-SOC-Dashboard
pip install -r requirements.txt
python soc_monitor.py
