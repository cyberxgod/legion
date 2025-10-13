# Auto Shopify CC Checker - Local Setup

## 📱 Termux Setup Instructions

### Step 1: Install Required Packages
```bash
pkg update && pkg upgrade
pkg install python
pkg install git
```

### Step 2: Install Python Dependencies
```bash
pip install flask flask-cors autoshopify
```

या फिर:
```bash
pip install -r requirements.txt
```

### Step 3: Run the Backend Server
```bash
python3 backend.py
```

Backend चलेगा: `http://localhost:5001`

### Step 4: Run the Frontend (New Terminal)
नया terminal खोलो और चलाओ:
```bash
cd Shopifyweb.py
python3 -m http.server 8081
```

Frontend चलेगा: `http://localhost:8081`

### Step 5: Open in Browser
अपने browser में खोलो: `http://localhost:8081`

---

## 🚀 Quick Start Scripts

### Backend चलाने के लिए:
```bash
bash run_backend.sh
```

### Frontend चलाने के लिए (दूसरे terminal में):
```bash
bash run_frontend.sh
```

---

## 📝 How It Works

1. **Frontend (HTML)** - `localhost:8081` पर चलता है
2. **Backend (Python)** - `localhost:5001` पर चलता है
3. Frontend से request जाती है Backend को
4. Backend `autoshopify` library use करके API call करता है
5. Response वापस Frontend को भेजता है

---

## ⚙️ API Configuration

Backend server `autoshopify.stormxcc` library use करता है:

```python
from autoshopify import stormxcc

resp = stormxcc(
    site="https://example.com",
    cc="card|mm|yyyy|cvv",
    proxy="host:port:user:pass",
    tries=2,
    timeout=30
)
```

---

## 📦 Files Structure

```
├── backend.py              # Python Flask backend server
├── Shopifyweb.py/         # Frontend files
│   └── index.html         # Main web interface
├── requirements.txt        # Python dependencies
├── run_backend.sh         # Backend start script
├── run_frontend.sh        # Frontend start script
└── README.md              # This file
```

---

## 🔐 Setup Telegram Notifications (Optional)

**अगर Telegram notifications चाहिए:**

1. [@BotFather](https://t.me/BotFather) से अपना bot बनाओ और token लो
2. `Shopifyweb.py/index.html` में line 700 पर token डालो:
```javascript
const BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN_HERE';
```
3. अपनी Telegram User ID डालो web interface में

## 🔧 Troubleshooting

**Backend नहीं चल रहा:**
```bash
pip install autoshopify
```

**CORS Error:**
- Make sure backend और frontend दोनों चल रहे हैं
- Backend में CORS enabled है

**Port already in use:**
- Backend port 5001 use करता है
- Frontend port 8081 use करता है
- अगर busy हो तो दूसरा port use करो

---

## 👨‍💻 Developer

**Name:** Rohit Vishal and sestraaa  
**Telegram:** [@rohitvishal9](https://t.me/rohitvishal9)  
**Channel:** [@OwnerxD_699](https://t.me/OwnerxD_699)
