# Bevan Li
# CS361 Microservice A task
# Microservice program
# Python 3.13

# Run as separate program and call using RESTful API call
# to http://localhost:PORT/trivia
# Modify PORT constant for changes if desired

from flask import Flask, request, jsonify
import requests
import re
import html
from bs4 import BeautifulSoup

app = Flask(__name__)
OMDB_API_KEY = 'e32c4c8f'  # Generated API key from OMDB (free imdb service)
PORT = 5555                # Port number


def get_imdb_id(title):
    # Search OMDb for the IMDb ID of the movie for use in URL later
    params = {'t': title, 'apikey': OMDB_API_KEY}
    response = requests.get("http://www.omdbapi.com/", params=params)
    data = response.json()
    return data.get('imdbID')


def fetch_trivia(imdb_id):
    # Fetches trivia using constructed URL and movie ID from API
    url = f'https://www.imdb.com/title/{imdb_id}/trivia'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    # Use regex to grab JSON from raw HTML response and find trivia
    match = re.search(r'<script[^>]+id="__NEXT_DATA__"[^>]*>(.*?)</script>', response.text, re.DOTALL)
    if not match:
        print("No embedded JSON found")
        return []
    raw_json = match.group(1)

    # Extract cardHtml values using regex
    matches = re.findall(r'"cardHtml":"(.*?)",', raw_json, re.DOTALL)
    trivia_items = [text for text in matches]

    print(f"Found {len(trivia_items)} trivia items via regex")
    return trivia_items


def clean_trivia(trivia_list):
    cleaned = []

    for raw in trivia_list:
        try:
            # This fixes double-escaped unicode
            raw = raw.encode().decode('unicode_escape')

            # Decode HTML entities like &quot;, &#39;, etc.
            decoded = html.unescape(raw)

            # Removes HTML tags
            stripped = BeautifulSoup(decoded, "html.parser").get_text()

            # Fix encoding of non-English characters (e.g., É → É)
            try:
                corrected = stripped.encode("latin1").decode("utf-8")
            except UnicodeEncodeError:
                corrected = stripped

            # Put letters back
            if corrected.strip():
                cleaned.append(corrected.strip())

        except Exception as e:
            print(f"Skipped an entry due to decode error: {e}")
            continue

    return cleaned


@app.route('/trivia', methods=['GET'])
def trivia_endpoint():
    title = request.args.get('title')
    if not title:
        return jsonify({'error': 'Missing "title" parameter'}), 400

    imdb_id = get_imdb_id(title)
    if not imdb_id:
        return jsonify({'error': f'Could not find IMDb ID for "{title}"'}), 404

    trivia_list = fetch_trivia(imdb_id)
    if not trivia_list:
        return jsonify({'error': f'No trivia found for "{title}"'}), 404

    return jsonify({'title': title, 'trivia': clean_trivia(trivia_list)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
