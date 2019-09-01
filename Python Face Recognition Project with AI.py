import face_recognition
from PIL import Image, ImageDraw
# Call any function in this code manually.

def FaceCount(path):
    image = face_recognition.load_image_file(path)
    face_locations = face_recognition.face_locations(image)
    print("The number of faces in your image is " + str(len(face_locations)) + "!")

def GetFaces(path):
    image = face_recognition.load_image_file(path)
    face_locations = face_recognition.face_locations(image)
    for face_location in face_locations:
        top, right, bottom, left = face_location
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.show()

def Similarity(path1, path2):
    person1_image = face_recognition.load_image_file(path1)
    person2_image = face_recognition.load_image_file(path2)

    person1_encoding = face_recognition.face_encodings(person1_image)[0]
    person2_encoding = face_recognition.face_encodings(person2_image)[0]

    results = face_recognition.compare_faces([person1_encoding], person2_encoding)
    print(results)


def Identify(Known1, Known2, TestPath):
    person1_image = face_recognition.load_image_file(Known1)
    person2_image = face_recognition.load_image_file(Known2)

    person1_encoding = face_recognition.face_encodings(person1_image)[0]
    person2_encoding = face_recognition.face_encodings(person2_image)[0]

    # Create array of encodings and names
    known_face_encodings = [
        person1_encoding,
        person2_encoding
    ]
    known_face_names = [
        "Bill Gates",
        "Steve Jobs"
    ]

    # Load the Image to find these faces in.
    test_image = face_recognition.load_image_file(TestPath)

    # Find Faces in test_image.
    face_locations = face_recognition.face_locations(test_image)
    face_encodings = face_recognition.face_encodings(test_image, face_locations)

    # Convert to Python Image Library Format.
    pil_image = Image.fromarray(test_image)

    # Create an ImageDraw instance.
    draw = ImageDraw.Draw(pil_image)

    # Loop through faces in test image.
    for(top,right,bottom,left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown Person"

        # If any faces match.
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
        # Draw Box.
        draw.rectangle(((left, top), (right, bottom)), width=10, outline=(255, 0, 0))

        # Draw Label.
        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(255, 0, 0), outline=(255, 0, 0))
        draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))
    del draw
    # Display image.
    pil_image.show()
    # Save image.
    pil_image.save("identify.jpg")


















