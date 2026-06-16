# 🚀 PyTelegram Messenger

**A beautiful, real-time messaging app inspired by Telegram**, built with **Python + Flask + Socket.IO**.

![Telegram-like Chat](https://via.placeholder.com/800x400/0088cc/ffffff?text=PyTelegram+Interface)

## ✨ Features

- **Real-time messaging** with WebSockets (instant delivery)
- **Persistent chat history** using SQLite
- **Modern Telegram-style UI** (dark theme, message bubbles, timestamps)
- **Multiple browser support** — chat together in real-time
- **Docker support** for easy deployment
- **Professional CI/CD** with GitHub Actions (linting, tests, Docker build)
- Ready for extensions: user auth, multiple rooms, file sharing, desktop app

## 🛠️ Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/ArseniyKB/messenger.git
cd messenger
pip install -r requirements.txt
```

### 2. Run the App

```bash
python run.py
```

Open **http://localhost:5000** in **multiple tabs** or browsers.

Type a username and start sending messages — they appear instantly for everyone!

### Using Docker (Recommended for Production)

```bash
docker build -t pytelegram-messenger .
docker run -p 5000:5000 pytelegram-messenger
```

## 🏗️ Project Structure

```
messenger/
├── app/                  # Core application
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── events.py
├── templates/            # HTML templates
│   └── index.html
├── static/               # CSS, JS, images
├── tests/                # Unit tests
├── .github/workflows/    # CI/CD pipelines
├── Dockerfile
├── requirements.txt
├── run.py
└── README.md
```

## 🚀 Deployment Options

- **Render / Railway / Fly.io** — See `.github/workflows/deploy.yml`
- **Docker** — One-command deploy anywhere
- **Heroku** / VPS — Easy with Gunicorn

## 🧪 Development

```bash
pip install -r requirements-dev.txt
pytest
ruff check .
```

## 🔮 Future Enhancements

- User registration & login
- Multiple chat rooms
- Emoji picker & reactions
- File/image sharing
- Desktop version with CustomTkinter
- Online users list

## 🤝 Contributing

Pull requests are welcome! Feel free to open issues for bugs or feature requests.

---

**Made with ❤️ using Python & Grok**

Star the repo if you like it! ⭐