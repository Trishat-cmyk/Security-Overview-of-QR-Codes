import cv2
from pyzbar.pyzbar import decode
from url_checker import analyze_url
from upi_validator import validate_upi_qr

def scan_qr():
    cap = cv2.VideoCapture(0)
    print("[INFO] QR Security Scanner Started (Press 'q' to quit)")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        for qr in decode(frame):
            data = qr.data.decode("utf-8")
            print("\n[QR DATA]", data)

            # 🔀 Decision logic
            if data.startswith("upi://"):
                validate_upi_qr(data)
            elif data.startswith("http://") or data.startswith("https://"):
                analyze_url(data)
            else:
                print("[RESULT] ❌ Unknown or Unsupported QR Code\n")

            cap.release()
            cv2.destroyAllWindows()
            return

        cv2.imshow("QR Security Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

scan_qr()
