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
        except ValueError:
            return redirect(url_for('home'))
#@app.route('/crop', methods=['POST'])
#def crop():
    #image_file = request.files['image']
  #  selected_option = request.form['option']

    # Simpan gambar yang diunggah
   # image_path = "static/uploaded_image.jpg"
    #image_file.save(image_path)

    # Load gambar
    #image = Image.open(image_path)

   # size = request.form['size']
    #position = request.form['position']

    # Baca gambar yang diupload
   # image = Image.open('static/uploaded_image.jpg')


    if selected_option == 'option1':
        cropped_image = image.crop((0, 0, 200, 200))
    elif selected_option == 'option2':
        cropped_image = image.crop((image.width // 2 - 100, 0, image.width // 2 + 100, 200))
    elif selected_option == 'option3':
        cropped_image = image.crop((image.width - 200, 0, image.width, 200))
    elif selected_option == 'option4':
        cropped_image = image.crop((0, image.height // 2 - 100, 200, image.height // 2 + 100))
    elif selected_option == 'option5':
        cropped_image = image.crop((image.width // 2 - 100, image.height // 2 - 100, image.width // 2 + 100, image.height // 2 + 100))
    elif selected_option == 'option6':
        cropped_image = image.crop((image.width - 200, image.height // 2 - 100, image.width, image.height // 2 + 100))
    elif selected_option == 'option7':
        cropped_image = image.crop((0, image.height - 200, 200, image.height))
    elif selected_option == 'option8':
        cropped_image = image.crop((image.width // 2 - 100, image.height - 200, image.width // 2 + 100, image.height))
    elif selected_option == 'option9':
        cropped_image = image.crop((image.width - 200, image.height - 200, image.width, image.height))

    # Simpan gambar hasil cropping dengan nama yang unik
    cropped_image_path = "static/cropped_image.jpg"
    cropped_image.save(cropped_image_path)

    return render_template('result.html', cropped_image_path=cropped_image_path)


    #top_left = image.crop((0, 0, 200, 200))
    #top_center = image.crop((image.width // 2 - 100, 0, image.width // 2 + 100, 200))
    #top_right = image.crop((image.width - 200, 0, image.width, 200))
    #center_left = image.crop((0, image.height // 2 - 100, 200, image.height // 2 + 100))
    #center = image.crop((image.width // 2 - 100, image.height // 2 - 100, image.width // 2 + 100, image.height // 2 + 100))
    #center_right = image.crop((image.width - 200, image.height // 2 - 100, image.width, image.height // 2 + 100))
    #bottom_left = image.crop((0, image.height - 200, 200, image.height))
    #bottom_center = image.crop((image.width // 2 - 100, image.height - 200, image.width // 2 + 100, image.height))
    #bottom_right = image.crop((image.width - 200, image.height - 200, image.width, image.height))


    # Simpan gambar hasil crop
    #top_left.save('static/top_left.jpg')
    #top_center.save('static/top_center.jpg')
    #top_right.save('static/top_right.jpg')
    #center_left.save('static/center_left.jpg')
    #center.save('static/center.jpg')
    #center_right.save('static/center_right.jpg')
    #bottom_left.save('static/bottom_left.jpg')
    #bottom_center.save('static/bottom_center.jpg')
    #bottom_right.save('static/bottom_right.jpg')

    #return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
