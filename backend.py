from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST', 'GET'])
def check_card():
    if request.method == 'POST':
        data = request.get_json()
        site = data.get('site', '')
        cc = data.get('cc', '')
        proxy = data.get('proxy', '')
    else:
        site = request.args.get('site', '')
        cc = request.args.get('cc', '')
        proxy = request.args.get('proxy', '')

    if not site or not cc:
        return jsonify({
            'Response': 'Error: Site and CC required',
            'Status': 400
        }), 400

    try:
        api_url = "https://autoshopifyxd.onrender.com/index.php"
        params = {
            'site': site,
            'cc': cc
        }
        if proxy:
            params['proxy'] = proxy

        response = requests.get(api_url, params=params, timeout=30)
        
        return jsonify({
            'Response': response.text,
            'Status': response.status_code
        })

    except Exception as e:
        return jsonify({
            'Response': f'Error: {str(e)}',
            'Status': 500
        }), 500

if __name__ == '__main__':
    print("Server running on http://localhost:5001")
    app.run(host='0.0.0.0', port=5001, debug=True)
