from flask import Flask, render_template
import random
import listy

app = Flask(__name__)

# Define your image and string dictionary
listy_data = listy.data


# Define the route for your home page
@app.route('/')
def home():
    # Get a random key from your image and string dictionary
    random_key = random.choice(list(listy_data.keys()))

    # Render the home template with the randomly selected image and text
    return render_template('home.html', image=listy_data[random_key]["src"], alt=listy_data[random_key]["alt"],
                           text=listy_data[random_key]["text"])

# Define the route for handling form submissions
@app.route('/get_random', methods=['POST'])
def get_random():
    # Get a random key from your image and string dictionary
    random_key = random.choice(list(listy_data.keys()))

    # Redirect back to the home page with the randomly selected image and text
    return render_template('home.html', image=listy_data[random_key]["src"], alt=listy_data[random_key]["alt"], text=listy_data[random_key]["text"])


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
