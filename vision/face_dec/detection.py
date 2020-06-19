import face_recognition
import cv2
import numpy as np

video = cv2.VideoCapture(0)

#load img and learn to recognize
james_img = face_recognition.load_image_file("james.jpg")
james_encoding = face_recognition.face_encodings(james_img)[0]

#arrays of known encodings & names
known_faces_encodings = [
	james_encoding
]
known_names = [
	"James"
]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:

	#grab a frame
	ret, frame = video_capture.read()

	#resize to 1/4 (faster)
	frame_small = cvs.resize(frame, (0,0), fx=0.25, fy=0.25)

	#convert from bgr (openCV uses) to rgb (face rec uses)
	frame_small_rgb = frame_small[:, :, ::-1]

	#process evry other frame to save time
	if process_this_frame:
		#find all faces & encodings in frame
		face_locations = face_recognition.face_locations(frame_small_rgb)
		face_encodings = face_recognition.face_encodings(frame_small_rgb, face_locations)

		face_names = []
		for face_encoding in face_encodings:
			matches = face_recognition.compare_faces(known_faces_encodings, face_encoding)
			name = 'Unknown'

			face_distances = face_recognition.face_distance(known_faces_encodings, face_encoding)
			best_match_index = np.argmin(face_distances)
			if matches[best_match_index]:
				name = known_names[best_match_index]

			face_names.append(name)

	process_this_frame = not process_this_frame

	for (top,right,bottom,left), name in zip(face_locations, face_names):
		print(name)

	if (input() == 'quit'):
		break

video_capture.release()
cv2.destroyAllWindows()
exit()