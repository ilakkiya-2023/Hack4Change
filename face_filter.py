# import cv2
# import dlib
# import numpy as np

# # Load the face detector
# detector = dlib.get_frontal_face_detector()
# # Load the face landmark predictor
# predictor = dlib.shape_predictor(dlib.shape_predictor("shape_predictor_68_face_landmarks.dat"))

# def apply_face_filter(video_path, output_path, filter_image_path):
#     cap = cv2.VideoCapture(video_path)
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#     out = cv2.VideoWriter(output_path, fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

#     filter_img = cv2.imread(filter_image_path, -1)  # Load filter image with alpha channel

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = detector(gray)

#         for face in faces:
#             landmarks = predictor(gray, face)
#             (x, y, w, h) = (face.left(), face.top(), face.width(), face.height())

#             # Apply filter image
#             filter_resized = cv2.resize(filter_img, (w, h), interpolation=cv2.INTER_AREA)
#             for i in range(3):
#                 frame[y:y+h, x:x+w, i] = np.where(filter_resized[:, :, 3] == 0,
#                                                    frame[y:y+h, x:x+w, i],
#                                                    filter_resized[:, :, i])

#         out.write(frame)

#     cap.release()
#     out.release()
#     cv2.destroyAllWindows()

# # # Example usage
# # apply_face_filter('input_video.mp4', 'output_video.mp4', 'filter.png')
