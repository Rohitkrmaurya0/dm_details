from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    # Scrape data
    url = "https://jaunpur.nic.in/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    dm_info_container = soup.find("div", class_="khowMinisterBox")
    dm_name_container = dm_info_container.find("div", class_="MinisterProfile")
    dm_image_container = dm_info_container.find("div", class_="khowMinisterBoxImg")

    dm_name_element = dm_name_container.find("span", class_="Pdesg")
    dm_image_url = dm_image_container.find("img")["src"]
    dm_name = dm_name_element.get_text()

    # Render the template with scraped data
    return render_template('dm_info.html', dm_name=dm_name, dm_image_url=dm_image_url)

if __name__ == '__main__':
    # app.debug = True
    app.run()
