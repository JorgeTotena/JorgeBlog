# Angelas's solution https://gist.github.com/angelabauer/f08f36c04065969f539f133f3b01832b
from flask import Flask, render_template, request, url_for, redirect
import requests
from post import Post

blog_url = "https://api.npoint.io/df95913612f01c28d4ec"
response = requests.get(url=blog_url)
all_posts = response.json()
posts = [Post(post["id"], post["title"], post["subtitle"], post["body"], post["date"], post["author"]) for post in all_posts]
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=posts)

@app.route('/post/<int:num>')
def get_post(num):
    for blog_post in posts:
        requested_post = None
        if blog_post.id == num:
            requested_post = blog_post
            return render_template("post.html", post=requested_post)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods = ['GET','POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html")
    if request.method == 'POST':
        username = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        # return redirect(url_for("receive_data"))
        return render_template("contact.html")

# @app.route('/form-entry', methods = ['POST'])
# def receive_data():
#     username = request.form['name']
#     email = request.form['email']
#     phone = request.form['phone']
#     message = request.form['message']
#     #return redirect(url_for("receive_data"))
#     return render_template("form-entry.html")



if __name__ == "__main__":
    app.run(debug=True)
