import face_recognition
import numpy

picture_of_me = face_recognition.load_image_file("KVEL.jpg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

# my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

unknown_picture = face_recognition.load_image_file("22.jpeg")
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

# Now we can see the two face encodings are of the same person with `compare_faces`!

results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)


face_distances = face_recognition.face_distance([my_face_encoding], unknown_face_encoding)

face_match_percentage = (1-face_distances)*100

for i, face_distance in enumerate(face_distances):
    print("The test image has a distance of {:.2} from known image #{}".format(face_distance, i))

    print("- comparing with a tolerance of 0.6? {}".format(face_distance < 0.6))

    print(numpy.round(face_match_percentage, 4))  # upto 4 decimal places