import cv2, time

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
subtractor = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=25, detectShadows=True)

MOTION_PIXELS = 1500     # how many changed pixels count as motion (tune this)
COOLDOWN = 10            # seconds of stillness before ACTIVE -> IDLE
DEEP_IDLE_AFTER = 30     # use 30 sec for testing; change to 1800 (30 min) later

state = "idle"
last_motion = time.time()

while True:
    ok, frame = cap.read()
    if not ok:
        continue

    small = cv2.resize(frame, (320, 180))
    mask = subtractor.apply(small)
    _, mask = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)  # drops shadow pixels
    mask = cv2.medianBlur(mask, 5)                              # removes speckle noise
    changed = cv2.countNonZero(mask)
    motion = changed > MOTION_PIXELS

    now = time.time()
    prev = state
    if motion:
        last_motion, state = now, "active"
    elif state == "active" and now - last_motion > COOLDOWN:
        state = "idle"
    elif state == "idle" and now - last_motion > DEEP_IDLE_AFTER:
        state = "deep_idle"

    if state != prev:
        print(time.strftime("%H:%M:%S"), prev, "->", state)

    cv2.putText(frame, f"{state.upper()}  changed={changed}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    cv2.imshow("camera", frame)
    cv2.imshow("motion mask", mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()