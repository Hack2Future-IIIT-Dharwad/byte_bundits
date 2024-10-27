<<<<<<< HEAD
import os
from flask import Flask, request, render_template, send_file
from gfpgan import GFPGANer
import cv2

app = Flask(__name__)

# Load GFPGAN model
model_path = 'models/GFPGANv1.3.pth'
gfpganer = GFPGANer(
    model_path=model_path,
    upscale=4, 
    arch='clean',  
    channel_multiplier=2,  
    bg_upsampler=None
)

@app.route('/')
def home():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return "No file part"

    file = request.files['image']
    if file.filename == '':
        return "No selected file"

    # Save the uploaded image in 'uploads' folder
    input_image_path = os.path.join('uploads', file.filename)
    file.save(input_image_path)

    # Process the image with GFPGAN model
    input_img = cv2.imread(input_image_path, cv2.IMREAD_COLOR)
    result = gfpganer.enhance(input_img, has_aligned=False, only_center_face=False, paste_back=True)

    if isinstance(result, tuple) and len(result) == 3:
        cropped_faces, restored_img = result[0], result[2]
        
        # Save the enhanced image to the 'output_image' folder
        output_folder = 'output_image'
        os.makedirs(output_folder, exist_ok=True)
        output_image_path = os.path.join(output_folder, 'final_output.png')
        cv2.imwrite(output_image_path, restored_img)

        # Send the enhanced image back as a downloadable file
        return send_file(output_image_path, as_attachment=True)
        # return render_template("upload.html",name='final_output.png')
    else:
        return "Unexpected result structure from enhance method."
if __name__ == '__main__':
    # Ensure required directories are created
    os.makedirs('uploads', exist_ok=True)
    os.makedirs('output_image', exist_ok=True)
    app.run(debug=True)
=======
import os
from flask import Flask, request, render_template, send_file
from gfpgan import GFPGANer
import cv2

app = Flask(__name__)

# Load GFPGAN model
model_path = 'models/GFPGANv1.3.pth'
gfpganer = GFPGANer(
    model_path=model_path,
    upscale=4, 
    arch='clean',  
    channel_multiplier=2,  
    bg_upsampler=None
)

@app.route('/')
def home():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return "No file part"

    file = request.files['image']
    if file.filename == '':
        return "No selected file"

    # Save the uploaded image in 'uploads' folder
    input_image_path = os.path.join('uploads', file.filename)
    file.save(input_image_path)

    # Process the image with GFPGAN model
    input_img = cv2.imread(input_image_path, cv2.IMREAD_COLOR)
    result = gfpganer.enhance(input_img, has_aligned=False, only_center_face=False, paste_back=True)

    if isinstance(result, tuple) and len(result) == 3:
        cropped_faces, restored_img = result[0], result[2]
        
        # Save the enhanced image to the 'output_image' folder
        output_folder = 'output_image'
        os.makedirs(output_folder, exist_ok=True)
        output_image_path = os.path.join(output_folder, 'final_output.png')
        cv2.imwrite(output_image_path, restored_img)

        # Send the enhanced image back as a downloadable file
        return send_file(output_image_path, as_attachment=True)
        # return render_template("upload.html",name='final_output.png')
    else:
        return "Unexpected result structure from enhance method."
if __name__ == '__main__':
    # Ensure required directories are created
    os.makedirs('uploads', exist_ok=True)
    os.makedirs('output_image', exist_ok=True)
    app.run(debug=True)
>>>>>>> 88f1ca129313f9b4f38c0d71d8d3f5eca2005956
