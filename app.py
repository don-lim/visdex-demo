# Import necessary modules
import os
import subprocess  # Add this line to import the subprocess module
import uuid  # Add this import for generating unique filenames
import base64  # Import base64 module for encoding images from non-public directory
from flask import Flask, render_template, send_from_directory, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/<string:name>/")
def say_hello(name):
    return f"Hello {name}!"

# Route to serve CSS files from /public/css
@app.route("/css/<path:filename>")
def serve_css(filename):
    return send_from_directory("public/css", filename)

# Route to serve JS files from /public/js
@app.route("/js/<path:filename>")
def serve_js(filename):
    return send_from_directory("public/js", filename)

# Route to serve img files from /public/img
@app.route("/img/<path:filename>")
def serve_img(filename):
    return send_from_directory("public/img", filename)

# Define a route to handle file uploads and image processing
@app.route("/upload", methods=["POST"])
def upload_file():
    try:
        # Get the uploaded file
        uploaded_file = request.files["image"]

        if uploaded_file.filename != "":
            # Generate a unique numeric filename using a combination of timestamp and random number
            unique_filename = f"{uuid.uuid4().time}{uuid.uuid4().int}"
            # Get the file extension
            file_extension = os.path.splitext(uploaded_file.filename)[-1]
            # Combine the unique filename and the original file extension
            unique_filename_with_extension = f"{unique_filename}{file_extension}"
            # Save the file with the unique filename
            file_path = os.path.join("data/uploads", unique_filename_with_extension)
            uploaded_file.save(file_path)

            # Display the uploaded image on the page
            # image_url = f"/{file_path}"
            image_url = f""

            # Here, you can invoke 'search.py' with the uploaded image if needed

            # Return a JSON response with the image URL
            return jsonify({"success": True, "message": "File uploaded successfully!", "image_url": image_url})

        else:
            return jsonify({"success": False, "message": "No file uploaded!"})

    except Exception as e:
        return jsonify({"success": False, "message": f"Error: {str(e)}"})

# Define a route to handle similarity search (route to 'search.py')
@app.route("/search", methods=["POST"])
def search():
    try:
        # Get the uploaded image file
        uploaded_file = request.files["image"]
        if uploaded_file.filename != "":
            with open("search.py", "r") as search_file:
                search_code = search_file.read()
                exec(search_code, globals())
                # 'similar_products_json' should be available in globals()
                # Create a list to store base64 encoded images
                base64_images = []
                # Loop through similar products and encode each image
                for product in json.loads(similar_products_json):
                    #img_file_path = os.path.join("data/sampledataset", product["imgFilePath"])
                    img_file_path = product["imgFilePath"]
                    with open(img_file_path, "rb") as image_file:
                        image_data = image_file.read()
                        base64_image = base64.b64encode(image_data).decode("utf-8")
                        base64_images.append(base64_image)

                # Include the base64 encoded images in the JSON response
                response_data = {
                    "success": True,
                    "results": json.loads(similar_products_json),
                    "image_base64": base64_images  # Add this to include the images as base64
                }
                return jsonify(response_data)
        else:
            return jsonify({"success": False, "message": "No file uploaded!"})

    except Exception as e:
        return jsonify({"success": False, "message": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run()
