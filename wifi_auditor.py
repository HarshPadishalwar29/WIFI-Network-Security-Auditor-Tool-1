#!/usr/bin/env python3
"""
Simple and Easy WIFI Network Security Auditor Tool
Created by Harsh Padishalwar
"""

import os
import subprocess
import time
import sys

def print_banner():
    print("""
    ╔═══════════════════════════════════════════════╗
    ║        WIFI SECURITY AUDITOR TOOL             ║
    ║              Created by: HP                   ║
    ╚═══════════════════════════════════════════════╝
    """)

def check_root():
    """Check if script is running as root"""
    if os.geteuid() != 0:
        print("❌ ERROR: This tool must be run as root!")
        print("Please run: sudo python3 wifi_auditor.py")
        sys.exit(1)

def main_menu():
    """Display main menu options"""
    print("\n" + "="*50)
    print("           MAIN MENU")
    print("="*50)
    print("1. Scan for WiFi Networks")
    print("2. Check Network Interface Status")
    print("3. Monitor Mode Utilities")
    print("4. 🔐 Detailed Security Analysis")
    print("5. Security Recommendations")
    print("6. About This Tool")
    print("7. Exit")
    print("="*50)
    
    choice = input("\nEnter your choice (1-7): ")
    return choice

def scan_networks():
    """Scan for available WiFi networks"""
    print("\n📡 Scanning for WiFi networks...")
    print("This may take 10-15 seconds...")
    
    try:
        # First check interfaces
        interface_check = subprocess.run(['iw', 'dev'], capture_output=True, text=True)
        
        if 'Interface' not in interface_check.stdout:
            print("\n❌ No wireless interfaces found!")
            print("\n💡 Solutions:")
            print("1. Run: sudo ip link set wlan0 up")
            print("2. Check if WiFi adapter is connected")
            print("3. Restart NetworkManager: sudo systemctl restart NetworkManager")
            input("\nPress Enter to continue...")
            return
        
        # Using iwlist to scan for networks
        result = subprocess.run(['iwlist', 'scan'], capture_output=True, text=True, timeout=20)
        
        if result.returncode == 0:
            print("\n✅ Scan completed!")
            print("\nFound networks (showing first 5):")
            
            # Simple parsing of iwlist output
            lines = result.stdout.split('\n')
            networks_found = 0
            
            for i, line in enumerate(lines):
                if 'ESSID:' in line and networks_found < 5:
                    essid = line.split('ESSID:')[1].strip().strip('"')
                    if essid:  # Only show non-empty ESSIDs
                        networks_found += 1
                        print(f"   {networks_found}. {essid}")
            
            if networks_found == 0:
                print("   No networks found or interface not available")
                print("\n💡 Try these solutions:")
                print("   - Run: sudo ip link set wlan0 up")
                print("   - Check WiFi adapter is not blocked: rfkill unblock wifi")
                print("   - Restart network: sudo systemctl restart NetworkManager")
        else:
            print("❌ Scan failed. Make sure you have a WiFi interface.")
            print("You might need to use: sudo ip link set [interface] up")
            
    except subprocess.TimeoutExpired:
        print("❌ Scan timed out. Try again.")
    except Exception as e:
        print(f"❌ Error during scan: {e}")
    
    input("\nPress Enter to continue...")

def check_interfaces():
    """Check available network interfaces"""
    print("\n🔍 Checking network interfaces...")
    
    try:
        # Show network interfaces
        result = subprocess.run(['ip', 'link', 'show'], capture_output=True, text=True)
        print("\nNetwork Interfaces:")
        print("="*40)
        
        lines = result.stdout.split('\n')
        wireless_found = False
        
        for line in lines:
            if 'wl' in line or 'wlan' in line:
                print(f"📶 {line.strip()}")
                wireless_found = True
            elif 'eth' in line or 'ethernet' in line.lower():
                print(f"🔗 {line.strip()}")
            elif 'lo:' in line:
                print(f"🔄 {line.strip()}")
        
        if not wireless_found:
            print("❌ No wireless interfaces found!")
            print("\n💡 Solutions:")
            print("1. Check if WiFi adapter is connected")
            print("2. Run: sudo ip link set wlan0 up")
            print("3. Check: rfkill list (if blocked, run: rfkill unblock wifi)")
        
        print("\n💡 Tip: Look for interfaces starting with 'wl' (wireless)")
        
    except Exception as e:
        print(f"❌ Error checking interfaces: {e}")
    
    input("\nPress Enter to continue...")

def monitor_mode_menu():
    """Submenu for monitor mode operations"""
    print("\n" + "="*50)
    print("        MONITOR MODE UTILITIES")
    print("="*50)
    print("1. Check Monitor Mode Capability")
    print("2. List Available Interfaces for Monitoring")
    print("3. Back to Main Menu")
    
    choice = input("\nEnter your choice (1-3): ")
    
    if choice == '1':
        check_monitor_capability()
    elif choice == '2':
        list_monitor_interfaces()
    elif choice == '3':
        return
    else:
        print("❌ Invalid choice!")

def check_monitor_capability():
    """Check if interfaces support monitor mode"""
    print("\n🔧 Checking monitor mode capability...")
    
    try:
        result = subprocess.run(['iw', 'list'], capture_output=True, text=True)
        
        if "monitor" in result.stdout.lower():
            print("✅ Your wireless interface supports monitor mode!")
            print("\nThis means you can perform advanced security testing.")
        else:
            print("❌ Monitor mode not supported or no wireless interface found")
            
    except Exception as e:
        print(f"❌ Error checking capability: {e}")
    
    input("\nPress Enter to continue...")

def list_monitor_interfaces():
    """List interfaces that can be used for monitoring"""
    print("\n📋 Available wireless interfaces:")
    
    try:
        result = subprocess.run(['iw', 'dev'], capture_output=True, text=True)
        print(result.stdout)
        
        if not result.stdout.strip():
            print("❌ No wireless interfaces found!")
        
    except Exception as e:
        print(f"❌ Error listing interfaces: {e}")
    
    input("\nPress Enter to continue...")

def analyze_network_security():
    """Detailed WiFi security analysis"""
    print("\n" + "="*50)
    print("        DETAILED SECURITY ANALYSIS")
    print("="*50)
    
    print("\n🔍 Scanning networks with security details...")
    print("This may take 20-30 seconds...")
    
    try:
        # Network scan with security information
        result = subprocess.run(['nmcli', '-f', 'SSID,SECURITY,SIGNAL', 'dev', 'wifi'], 
                              capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print("\n📊 NETWORK SECURITY ANALYSIS:")
            print("="*60)
            
            lines = result.stdout.split('\n')
            networks_found = 0
            
            for line in lines[1:]:  # Skip header
                if line.strip() and networks_found < 10:  # Limit to 10 networks
                    networks_found += 1
                    parts = line.strip().split()
                    if len(parts) >= 2:
                        ssid = parts[0]
                        security = " ".join(parts[1:-1]) if len(parts) > 2 else " ".join(parts[1:])
                    else:
                        ssid = "Hidden"
                        security = "Unknown"
                    
                    # Security assessment
                    security_level = assess_security_level(security)
                    
                    print(f"\n📶 Network: {ssid}")
                    print(f"   🔒 Security: {security}")
                    print(f"   ⚡ Level: {security_level}")
                    
                    # Show recommendations
                    show_security_recommendations(security)
            
            if networks_found == 0:
                print("\n❌ No networks found or scanning not available")
                print("\n💡 Alternative scan method...")
                alternative_scan()
                
        else:
            print("❌ Could not scan using nmcli")
            print("\n💡 Trying alternative method...")
            alternative_scan()
            
    except subprocess.TimeoutExpired:
        print("❌ Scan timed out")
    except Exception as e:
        print(f"❌ Error during analysis: {e}")
        print("\n💡 Trying alternative method...")
        alternative_scan()
    
    input("\nPress Enter to continue...")

def assess_security_level(security_info):
    """Determine security level based on encryption type"""
    security_info = security_info.upper()
    
    if 'WPA3' in security_info:
        return "✅ STRONG (Excellent)"
    elif 'WPA2' in security_info and 'AES' in security_info:
        return "✅ STRONG (Good)"
    elif 'WPA2' in security_info:
        return "🟡 MEDIUM (Acceptable)"
    elif 'WPA' in security_info:
        return "🟡 MEDIUM (Needs Upgrade)"
    elif 'WEP' in security_info:
        return "❌ WEAK (Immediately Change)"
    elif 'OPEN' in security_info or not security_info:
        return "❌ VERY WEAK (No Security!)"
    else:
        return "🟡 UNKNOWN (Check Manually)"

def show_security_recommendations(security_type):
    """Show specific recommendations for each security type"""
    security_type = security_type.upper()
    
    if 'WPA3' in security_type:
        print("   💡 Recommendation: Excellent! Maintain current settings")
        
    elif 'WPA2' in security_type:
        print("   💡 Recommendation: Good, but upgrade to WPA3 if available")
        print("   🔧 Action: Check router settings for WPA3 option")
        
    elif 'WPA' in security_type:
        print("   💡 Recommendation: Upgrade to WPA2/WPA3 immediately")
        print("   🔧 Action: Change encryption type in router settings")
        
    elif 'WEP' in security_type:
        print("   💡 Recommendation: CRITICAL - Change immediately!")
        print("   🔧 Action: WEP can be cracked in minutes - upgrade to WPA2")
        
    elif 'OPEN' in security_type or not security_type:
        print("   💡 Recommendation: EXTREMELY DANGEROUS!")
        print("   🔧 Action: Enable WPA2/WPA3 encryption with strong password")
        
    else:
        print("   💡 Recommendation: Check router security settings")

def alternative_scan():
    """Alternative scanning method if nmcli fails"""
    print("\n🔄 Trying alternative scan method...")
    try:
        result = subprocess.run(['iwlist', 'scan'], capture_output=True, text=True, timeout=20)
        
        if result.returncode == 0:
            print("\n📶 Found Networks (Basic Info):")
            lines = result.stdout.split('\n')
            networks_found = 0
            
            for line in lines:
                if 'ESSID:' in line and networks_found < 5:
                    essid = line.split('ESSID:')[1].strip().strip('"')
                    if essid:
                        networks_found += 1
                        print(f"   {networks_found}. {essid} - 🔒 Security: Unknown (Use router to check)")
            
            if networks_found == 0:
                print("   No networks found")
    except:
        print("   Alternative scan also failed")

def security_recommendations():
    """Display comprehensive security recommendations"""
    print("""
    🔐 COMPREHENSIVE WIFI SECURITY GUIDE:
    
    =============================================
    🎯 QUICK FIXES FOR WEAK NETWORKS:
    =============================================
    
    1. ❌ OPEN NETWORK (No Password):
       🔧 IMMEDIATE ACTION:
       • Go to router settings
       • Select Wireless Security section
       • Choose WPA2-Personal
       • Set strong password (12+ characters)
    
    2. ❌ WEP ENCRYPTION:
       🔧 IMMEDIATE ACTION:
       • Change encryption type to WPA2
       • Disable WPS
       • Update firmware
    
    =============================================
    📊 SECURITY LEVELS EXPLAINED:
    =============================================
    
    ✅ STRONG (WPA3):
       • Latest encryption standard
       • Government-level security
       • Future-proof
    
    ✅ GOOD (WPA2-AES):
       • Currently secure
       • Most common
       • Recommended for home use
    
    🟡 MEDIUM (WPA/WPA2-TKIP):
       • Needs upgrade
       • Some vulnerabilities
       • Better than WEP
    
    ❌ WEAK (WEP):
       • Can be cracked in 5-10 minutes
       • Change immediately
    
    ❌ VERY WEAK (Open):
       • Anyone can access
       • Personal data at risk
    
    =============================================
    🛡️ ADVANCED PROTECTION:
    =============================================
    
    • MAC Address Filtering: Only allow known devices
    • Hide SSID: Make network invisible
    • Guest Network: Separate network for visitors
    • Regular Updates: Update router firmware
    • Strong Password: Mix of uppercase, lowercase, numbers, symbols
    
    =============================================
    ⚠️ COMMON MISTAKES TO AVOID:
    =============================================
    
    • Using default router passwords
    • Simple passwords like 'password123'
    • Enabling WPS (vulnerable)
    • Enabling remote administration
    • Ignoring firmware updates
    """)
    input("\nPress Enter to continue...")

def about_tool():
    """Display information about the tool"""
    print("""
    🔐 WIFI SECURITY AUDITOR TOOL
    
    PURPOSE:
    This tool helps beginners understand WiFi security concepts
    and perform basic network auditing tasks.
    
    FEATURES:
    • Scan for available WiFi networks
    • Check network interface status
    • Verify monitor mode capability
    • Detailed security analysis (Weak/Strong networks)
    • Security recommendations and fixes
    
    ⚠️  IMPORTANT NOTES:
    • Only use on networks you own or have permission to test
    • This is for educational purposes
    • Always follow ethical hacking principles
    • Respect privacy and laws
    
    CREATOR: Harsh Padishalwar
    VERSION: 1.0
    """)
    input("\nPress Enter to continue...")

def main():
    check_root()
    print_banner()
    
    while True:
        choice = main_menu()
        
        if choice == '1':
            scan_networks()
        elif choice == '2':
            check_interfaces()
        elif choice == '3':
            monitor_mode_menu()
        elif choice == '4':
            analyze_network_security()
        elif choice == '5':
            security_recommendations()
        elif choice == '6':
            about_tool()
        elif choice == '7':
            print("\nThank you for using WIFI Security Auditor!")
            print("Stay secure! 👋")
            break
        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
