from flask import Flask, jsonify

from enrich import enrich_organization_data
from scarper import scrape_crunchbase_data
from utils import save_to_file, load_from_file
import os

app = Flask(__name__)

DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH")

@app.route('/scrape', methods=['GET'])
def scrape():
    organizations = scrape_crunchbase_data(DRIVER_PATH)
    save_to_file(organizations)
    return jsonify({"message": "Scraping completed.", "data": organizations})

@app.route('/enrich', methods=['GET'])
def enrich():
    organizations = load_from_file()
    for org in organizations:
        org["enrichment"] = enrich_organization_data(org)
    save_to_file(organizations)
    return jsonify({"message": "Enrichment completed.", "data": organizations})

@app.route('/organizations', methods=['GET'])
def get_organizations():
    organizations = load_from_file()
    return jsonify(organizations)

if __name__ == '__main__':
    app.run(debug=True)
