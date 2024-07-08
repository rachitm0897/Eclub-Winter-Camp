import mediapipe as mp
import cv2

mp_face_mesh = mp.solutions.face_mesh

face_mesh_images = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=2,
                                         min_detection_confidence=0.5, min_tracking_confidence=0.5)

mp_drawing = mp.solutions.drawing_utils

mp_drawing_styles = mp.solutions.drawing_styles

cam = cv2.VideoCapture(0)
while True:
    
    ignore, frame = cam.read()
    img_copy = frame[:,:,::-1].copy()
    face_mesh_results = face_mesh_images.process(frame[:,:,::-1])
    if face_mesh_results.multi_face_landmarks:

        for face_landmarks in face_mesh_results.multi_face_landmarks:

            mp_drawing.draw_landmarks(image=img_copy, 
                                    landmark_list=face_landmarks,connections=mp_face_mesh.FACEMESH_TESSELATION,
                                    landmark_drawing_spec=None, 
                                    connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style())
            
            mp_drawing.draw_landmarks(image=img_copy, landmark_list=face_landmarks,connections=mp_face_mesh.FACEMESH_CONTOURS,
                                    landmark_drawing_spec=None, 
                                    connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_contours_style())
    
    img_copy = cv2.cvtColor(img_copy, cv2.COLOR_RGB2BGR)
    cv2.imshow("frame", img_copy)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()