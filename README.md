# 🤖 Chatbot Using Flask and Gemini API

Welcome to the Chatbot project using Flask and the Gemini API! This project demonstrates how to build a chatbot that interacts with users through a web interface and utilizes the Gemini API for generating responses. The interactions are also stored in a local MySQL database.

## 📋 Requirements

To get started, you'll need to install the following Python libraries:

- `Flask`
- `google-generativeai`
- `pymysql`
- `json`
- `datetime`

You can install these libraries using pip:

```bash
pip install Flask google-generativeai pymysql
```
## 🗂️ Project Structure

- **`app.py`**: The main Flask application file.
- **`static/style.css`**: The CSS file for styling your web interface.
- **`templates/index.html`**: The HTML file for the frontend.
- **MySQL Database**: Connected to store chat history.

## Create a Virtual Environment

To set up a virtual environment, follow these steps:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
## Prepare Frontend

1. **Create `static/style.css` for your styles.**

2. **Create `templates/index.html` for your HTML template.**

   The folder structure should look like this:

project-root/
├── app.py
├── static/
│   └── style.css
└── templates/
    └── index.html
## 🚀 How It Works

1. **Frontend Interaction**: The user interacts with the chatbot through a web interface. The frontend is served by Flask and styled with `style.css`.

2. **User Input**: When a user submits their query, the input is sent to the Flask backend.

3. **Gemini API**: The backend uses the Gemini API to generate responses based on user input.

4. **Database Logging**: Each interaction is logged into the MySQL database, storing both user queries and the chatbot’s responses.

5. **Model Configuration**: You can modify the `app.py` file to use different models from the Gemini API if desired.

## 🌐 Accessing the Chatbot

Run the Flask application with:

```bash
python app.py
```

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## 📢 Feedback

If you encounter any issues or have suggestions, please reachout.
email - akashanandnai.56@gmail.com
github-kasshh56

Happy coding! 🚀




