import cv2
import mediapipe as mp

mp_face = mp.solutions.face_detection.FaceDetection()

def smart_vertical_crop(video_path, output_path):
    cap = cv2.VideoCapture(video_path)

    w = int(cap.get(3))
    h = int(cap.get(4))
    out_w = int(h * 9 / 16)

    out = cv2.VideoWriter(
        output_path,
        cv2.VideoWriter_fourcc(*"mp4v"),
        20,
        (out_w, h)
    )

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = mp_face.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        if results.detections:
            for det in results.detections:
                bbox = det.location_data.relative_bounding_box
                cx = int((bbox.xmin + bbox.width/2) * w)

                x1 = max(0, cx - out_w//2)
                x2 = x1 + out_w

                cropped = frame[:, x1:x2]
                out.write(cropped)
        else:
            center = w // 2
            cropped = frame[:, center-out_w//2:center+out_w//2]
            out.write(cropped)

    cap.release()
    out.release()

    return output_path