# 🔐 WiFi Security Auditor

A comprehensive, beginner-friendly Wi-Fi security auditing tool built in Python. This tool scans nearby wireless networks, identifies security protocols, evaluates encryption strength, and provides actionable recommendations to enhance network protection. Ideal for cybersecurity learners, ethical penetration testers (with authorization), and home network security assessments.

---

## ✅ Features

| Feature | Description |
|--------|-------------|
📡 **Network Discovery** | Scan and list available Wi-Fi networks  
🔐 **Security Assessment** | Detect WEP / WPA / WPA2 / WPA3 encryption types  
⚠️ **Vulnerability Detection** | Identify weak or open networks  
🛠 **Monitor Mode Check** | Verify if Wi-Fi adapter supports monitor mode  
🎯 **Beginner Friendly** | Clean menu-driven interface with guidance  
📚 **Educational Output** | Security suggestions & best practices  
🔁 **Dual Scan Methods** | Uses `iwlist` and `nmcli` for robust scanning  

---

## 🧠 How It Works

This tool performs:

- Wireless interface detection  
- Access point scanning  
- Encryption type classification  
- Security scoring  
- Recommended security actions  

---

## 🛠 Tech Stack

| Tool / Library | Purpose |
|----------------|--------|
Python 3 | Core scripting language  
`iw`, `iwlist` | Wireless scanning utilities  
`nmcli` | NetworkManager Wi-Fi scanning  
Bash utilities | System-level commands  

---

## 📦 Requirements

- **Linux OS** (Kali, Ubuntu, Parrot OS, etc.)
- **Python 3.8+**
- **Wireless Adapter**
  - Recommended: Supports monitor mode
- **Root / sudo privileges**

---

⬇️ Sample Menu
==================================================
               MAIN MENU
==================================================
1. Scan for WiFi Networks
2. Check Network Interface Status
3. Monitor Mode Utilities
4. Detailed Security Analysis
5. Security Recommendations
6. About This Tool
7. Exit
==================================================

---

📊 Example Output
Network: HomeNetwork
Security: WPA2
Level: STRONG
Recommendation: Good — upgrade to WPA3 if supported.

Network: CafeWiFi
Security: OPEN
Level: VERY WEAK
Recommendation: Extremely unsafe — avoid connecting.

---

🏆 Achievements

✅ Classifies Wi-Fi security levels accurately
✅ Provides clear security improvement steps
✅ Multi-method scanning for reliability
✅ Beginner-friendly & educational output
✅ Built-in troubleshooting messages

⚠️ Legal & Ethical Use

This tool is for:

✅ Learning cybersecurity
✅ Personal/home network auditing
✅ Authorized penetration testing

Do NOT scan networks without explicit permission.
Unauthorized scanning violates laws & privacy policies.

