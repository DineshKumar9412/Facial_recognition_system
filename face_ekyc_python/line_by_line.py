from flask import Flask, redirect, url_for, request,jsonify
import face_recognition

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def success():
   if request.method == 'POST':
      files = request.files.getlist("file")
      doc_file = files[0]
      selfie_file = files[1]
      return detect_faces_in_image(doc_file, selfie_file)

def detect_faces_in_image(doc, selfie):
   try:
      picture_of_me = face_recognition.load_image_file(doc)
      my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
      unknown_picture = face_recognition.load_image_file(selfie)
      unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

      is_same = False

      if len(unknown_face_encoding) > 0:
         face_found = True
         match_results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
         print(match_results)
         if match_results[0]:
            is_same = True
      # Return the result as json
      result = {
         "face_found_in_image": face_found,
         "isMatched": is_same
      }

      return jsonify(result)
   except:
      # Return the result as json
      result = {
         "face_found_in_image": False,
         "isMatched": False
      }
      return jsonify(result)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8008,debug = True)
