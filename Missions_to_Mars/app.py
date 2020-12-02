from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    site_info = mongo.db.site_info.find_one()
    return render_template("index.html", site_info=site_info)

@app.route("/scrape")
def scrape():
    site_info = mongo.db.site_info
    site_info_data = scrape_mars.scrape()
    site_info.update_one({}, site_info_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
