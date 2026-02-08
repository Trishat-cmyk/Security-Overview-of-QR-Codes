from urllib.parse import urlparse, parse_qs
import re

def validate_upi_qr(data):
    print("[INFO] Detected UPI QR Code")
    
    if not data.startswith("upi://pay"):
        print("[RESULT] ❌ Invalid UPI QR format\n")
        return

    parsed = urlparse(data)
    params = parse_qs(parsed.query)

    required_fields = ["pa", "pn", "cu"]

    for field in required_fields:
        if field not in params:
            print(f"[RESULT] ❌ Invalid UPI QR (Missing {field})\n")
            return

    pa = params["pa"][0]
    pn = params["pn"][0]
    cu = params["cu"][0]
    am = params.get("am", ["Not Specified"])[0]

    if not re.match(r"^[\w.-]+@[\w.-]+$", pa):
        print("[RESULT] ❌ Invalid UPI ID format\n")
        return

    if cu != "INR":
        print("[RESULT] ❌ Unsupported currency\n")
        return

    print("\n✅ VALID UPI QR CODE")
    print("----------------------")
    print(f"Payee Name : {pn}")
    print(f"UPI ID     : {pa}")
    print(f"Amount     : {am}")
    print(f"Currency   : {cu}\n")
