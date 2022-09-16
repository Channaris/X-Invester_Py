from flask import Flask

app = Flask(__name__)

@app.route('/flask', methods=['GET'])
def index():
    app.run('/test_post_lvisd.py')
    app.run('/test_post_ppth.py')
    app.run('/test_post_renthub.py')
    app.run('/test_post_thaihometown.py')


    return "Flask server"

if __name__ == "__main__":
    app.run(port=5000, debug=True)