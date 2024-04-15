import cv2
import mediapipe as mp
import json
import requests
import numpy as np

def load_json(file_path):
    # Load JSON file
    with open(file_path, "r") as file:
        json_data = file.read()

    data = json.loads(json_data)
    return data

def extract_facial_features(image_url):
    # Download the image
    try:
        response = requests.get(image_url)
        image_array = np.asarray(bytearray(response.content), dtype=np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    except requests.exceptions.InvalidSchema:
        image = cv2.imread(image_url)

    # Initialize MediaPipe FaceMesh
    mp_face_mesh = mp.solutions.face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1)

    # Convert the image to RGB format
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image with MediaPipe FaceMesh
    results = mp_face_mesh.process(image_rgb)

    # Extract facial landmarks from the results
    facial_landmarks = []
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            for landmark in face_landmarks.landmark:
                x = int(landmark.x * image.shape[1])
                y = int(landmark.y * image.shape[0])
                facial_landmarks.append((x, y))

    return facial_landmarks

def self_extract(img_path):
    facial_landmarks = extract_facial_features(img_path)
    return facial_landmarks

def meme_extract(range):
    json_file_path = "db.json"

    # Open the JSON file in read mode
    with open(json_file_path, "r") as file:
        # Read the contents of the file
        json_data = file.read()

    data = json.loads(json_data)
    poslinks = {}
    # Process the image URLs
    for pos, item in enumerate(data["_default"].values()):
        image_url = item["media"]
        facial_landmarks = extract_facial_features(image_url)
        if len(facial_landmarks):
            if pos >= range:
                break
            else:
                poslinks.update({image_url: facial_landmarks})

    # Convert poslinks dictionary to a JSON string
    poslinks_json = json.dumps(poslinks)

    with open("meme.json", "w") as memewrite:
        memewrite.write(poslinks_json)

    print("Extracting Done.")

def calculate_similarity(meme_landmarks, person_landmarks):
    # Calculate similarity using Euclidean distance
    dist = np.linalg.norm(np.array(meme_landmarks) - np.array(person_landmarks))
    similarity = 1 / (1 + dist)  # Invert the distance to get similarity score
    return similarity

def find_most_relevant_meme(meme_data, person_landmarks):
    best_matching_meme = None
    best_matching_score = 0

    # Process the meme data
    for image_url, meme_landmarks in meme_data.items():
        # Calculate the similarity between the person's facial landmarks and the meme's facial landmarks
        similarity = calculate_similarity(meme_landmarks, person_landmarks)
        if similarity > best_matching_score:
            best_matching_score = similarity
            best_matching_meme = image_url

    return best_matching_meme, best_matching_score

def countdata(thing):
    print(len(list(load_json(thing).keys())))