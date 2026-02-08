import cv2 
from pyzbar.pyzbar import decode
from url_checker import analyze_url

def scan_qr():
    cap = cv2.VideoCapture(0)
    print("[INFO] Scanning QR Code... Press 'q' to quit.")

    while True:
        _, frame = cap.read()
        decoded_objects = decode(frame)

        for obj in decoded_objects:
            data = obj.data.decode("utf-8")
            print(f"[QR DATA] {data}")
            analyze_url(data)
            cap.release()
            cv2.destroyAllWindows()
            return

        cv2.imshow("QR Code Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

scan_qr()
