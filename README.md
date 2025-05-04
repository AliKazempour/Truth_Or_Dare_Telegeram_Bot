
# Truth or Dare Telegram Bot 🎲

A Persian-language Telegram bot for playing **"Truth or Dare"** — built with Python and the `python-telegram-bot` library.

---

**Made by:** Ali Kazempour  
**University:** Shahed University  
**Term:** Spring 2022  
**Contact me on Telegram:** [https://t.me/A_Kazempour83](https://t.me/A_Kazempour83)

---

## 📌 Features

- Interactive commands to play Truth or Dare in Farsi
- Random question generation for both categories
- Friendly UI with Telegram's reply keyboard
- Inline help and exit support
- Clean logging and command handling

---

## 📽️ Watch It in Action

You can see a short screen recording of the bot in action [in this LinkedIn post](https://www.linkedin.com/posts/activity-7075063972437069824-_hfO?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAADAdZZIBFwdbQQtZ20qZdQTX8eLPwgZiUOc).

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone git@github.com:AliKazempour/Truth_Or_Dare_Telegeram_Bot.git
cd Truth_Or_Dare_Telegeram_Bot
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the bot token

Replace the line in the script:

```python
BOT_TOKEN: Final = "Token"
```

with your actual bot token from [BotFather](https://t.me/BotFather):

```python
BOT_TOKEN: Final = "YOUR_BOT_TOKEN"
```

### 4. Run the bot

```bash
python main.py
```

The bot will start polling and will be ready to interact with users.

---

## 💬 Available Commands

| Command  | Description                          |
| -------- | ------------------------------------ |
| /start   | Start the bot                        |
| /play    | Begin a new round of "Truth or Dare" |
| /truth   | Get a random truth question          |
| /courage | Get a random dare                    |
| /help    | Show help instructions               |
| /exit    | End the current game session         |

