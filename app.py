from flask import Flask, render_template, request, redirect, url_for
from PIL import Image

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return redirect(url_for('home'))
    
    image = request.files['image']
    if image.filename == '':
        return redirect(url_for('home'))

    # Simpan gambar yang diupload
    image.save('static/uploaded_image.jpg')

    return render_template('form.html')

@app.route('/crop', methods=['POST'])
def crop():
    selected_option = request.form['option']
    size = request.form['size']

    # Load gambar yang diunggah
    image_path = "static/uploaded_image.jpg"
    image = Image.open(image_path)

    # Validasi ukuran yang diinput tidak melebihi ukuran gambar
    
    image_width, image_height = image.size
    if size:
        try:
            crop_size = int(size)
            if crop_size > image_width or crop_size > image_height:
                raise ValueError("Ukuran melebihi dimensi gambar")
                x = y = crop_size
        except ValueError:
            return redirect(url_for('home'))
    
    if selected_option == 'option1':
        cropped_image = image.crop((0, 0, crop_size, crop_size))
    elif selected_option == 'option2':
        cropped_image = image.crop((image_width // 2 - crop_size // 2, 0, image_width // 2 + crop_size // 2, crop_size))
    elif selected_option == 'option3':
        cropped_image = image.crop((image_width - crop_size, 0, image_width, crop_size))
    elif selected_option == 'option4':
        cropped_image = image.crop((0, image_height // 2 - crop_size // 2, crop_size, image_height // 2 + crop_size // 2))
    elif selected_option == 'option5':
        cropped_image = image.crop((image_width // 2 - crop_size // 2, image_height // 2 - crop_size // 2, image_width // 2 + crop_size // 2, image_height // 2 + crop_size // 2))
    elif selected_option == 'option6':
        cropped_image = image.crop((image_width - crop_size, image_height // 2 - crop_size // 2, image_width, image_height // 2 + crop_size // 2))
    elif selected_option == 'option7':
        cropped_image = image.crop((0, image_height - crop_size, crop_size, image_height))
    elif selected_option == 'option8':
        cropped_image = image.crop((image_width // 2 - crop_size // 2, image_height - crop_size, image_width // 2 + crop_size // 2, image_height))
    elif selected_option == 'option9':
        cropped_image = image.crop((image_width - crop_size, image_height - crop_size, image_width, image_height))

    

    # Simpan gambar hasil cropping dengan nama yang unik
    cropped_image_path = "static/cropped_image.jpg"
    cropped_image.save(cropped_image_path)

    return render_template('result.html', cropped_image_path=cropped_image_path)


if __name__ == '__main__':
    app.run(debug=True)
