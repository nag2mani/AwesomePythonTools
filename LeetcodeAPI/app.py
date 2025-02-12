from flask import Flask, render_template, request
import requests

app = Flask(__name__)
BASE_URL = "https://alfa-leetcode-api.onrender.com/userProfile/"

@app.route('/', methods=['GET', 'POST'])
def index():
    user_data = None
    error = None
    
    if request.method == 'POST':
        username = request.form['username']
        if username:
            response = requests.get(BASE_URL + username)
            
            if response.status_code == 200:
                user_data = response.json()
                # print(user_data)
            else:
                error = "User not found or API issue."
    
    return render_template('index.html', user_data=user_data, error=error, username=username)

if __name__ == '__main__':
    app.run(debug=True)