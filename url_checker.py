import re
import requests 

def analyze_url(url):
    print("[INFO] Analyzing URL Security...")

    phishing_patterns = [
        r"free", r"login", r"verify", r"update",
        r"secure", r"account", r"bank"
    ]

    suspicious = False

    if not url.startswith("https://"):
        print("[WARNING] URL does not use HTTPS")
        suspicious = True

    for pattern in phishing_patterns:
        if re.search(pattern, url, re.IGNORECASE):
            print(f"[WARNING] Phishing keyword detected: {pattern}")
            suspicious = True

    try:
        response = requests.get(url, timeout=5)
        print("[INFO] URL is reachable")
    except:
        print("[ERROR] URL unreachable or suspicious")
        suspicious = True

    if suspicious:
        print("[RESULT] ❌ Potentially Malicious QR Code")
    else:
        print("[RESULT] ✅ QR Code Appears Safe")
