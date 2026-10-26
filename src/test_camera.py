import cv2, time

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    raise SystemExit("Camera could not be opened")

fails, frames, t0 = 0, 0, time.time()
while True:
    ok, frame = cap.read()
    if not ok:                      # camera still warming up, or a dropped frame
        fails += 1
        if fails > 50:
            print("Too many failed reads, giving up")
            break
        continue
    fails = 0
    frames += 1
    if frames == 1:
        print("Frame size:", frame.shape[1], "x", frame.shape[0])
    cv2.imshow("camera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

elapsed = time.time() - t0
print(f"Measured FPS: {frames / elapsed:.1f}")
cap.release()
cv2.destroyAllWindows()