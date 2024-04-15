from extract_funcs import *
from flask import Flask, render_template, request, send_from_directory
import os
import uuid

choice = input("Run App, Train, or count Training Data? (1/2/3): ")

if choice == "1":
    def get_meme(img_path):
        person_landmarks = self_extract(img_path)
        meme_data = load_json("meme.json")
        best_matching_meme, best_matching_score = find_most_relevant_meme(meme_data, person_landmarks)

        return best_matching_meme

    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('main.html')

    @app.route('/upload', methods=['POST'])
    def upload():
        photo = request.files['photo']
        if photo:
            # Generate a unique filename for the uploaded photo
            filename = str(uuid.uuid4()) + os.path.splitext(photo.filename)[1]
            photo.save(os.path.join('C:\\Users\\Dacha\\Documents\\Coding\\Python\\Flask\\Meme\\uploads', filename))
            link = os.path.join('C:\\Users\\Dacha\\Documents\\Coding\\Python\\Flask\\Meme\\uploads', filename)
            print(link)
            memelink = get_meme(link)
            return render_template('main.html', link=link, memelink=memelink)
        return 'No photo uploaded.'

    @app.route('/uploads/<path:filename>')
    def serve_file(filename):
        return send_from_directory('uploads', filename)

    if __name__ == '__main__':
        app.run(debug = True)

else:
    threshold = int(input("Training Threshold: "))
    if threshold <= 800:
        meme_extract(threshold)
    else:
        print("Threshold surpassed limit of 800.")

