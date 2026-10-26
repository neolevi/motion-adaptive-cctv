import cv2

backends = {"DSHOW": cv2.CAP_DSHOW, "MSMF": cv2.CAP_MSMF, "DEFAULT": cv2.CAP_ANY}
for name, backend in backends.items():
    for index in range(4):
        cap = cv2.VideoCapture(index, backend)
        ok, frame = cap.read() if cap.isOpened() else (False, None)
        print(f"{name:8} index {index}: opened={cap.isOpened()}  frame={'YES' if ok else 'no'}")
        cap.release()