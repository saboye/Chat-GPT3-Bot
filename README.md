

### <h1 align="center" style="color:blue;" id="heading">Chat GPT3 Bot</h1>

<p align="center">
  <img src="https://img.shields.io/github/contributors/saboye/Chat-GPT3-Bot?color=blue&logo=github&style=for-the-badge" alt="GitHub contributors">
  <img src="https://img.shields.io/github/forks/saboye/Chat-GPT3-Bot?logo=github&style=for-the-badge" alt="GitHub forks">
  <img src="https://img.shields.io/github/issues-raw/saboye/Chat-GPT3-Bot?style=for-the-badge" alt="GitHub issues">
  <img src="https://img.shields.io/github/license/saboye/Chat-GPT3-Bot?label=license&style=for-the-badge" alt="GitHub license">
  <img src="https://img.shields.io/github/last-commit/saboye/Chat-GPT3-Bot?style=for-the-badge" alt="GitHub last commit">
  <img src="https://img.shields.io/badge/Chat-GPT3-brightgreen?style=for-the-badge&logo=openai" alt="Chat GPT3">
  <img src="https://img.shields.io/badge/Framework-Flask-blue?style=for-the-badge&logo=flask" alt="Flask">
  <img src="https://img.shields.io/badge/Powered%20by-OpenAI-brightgreen?style=for-the-badge&logo=openai" alt="OpenAI">
  <img src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Language-JavaScript-yellow?style=for-the-badge&logo=javascript" alt="JavaScript">
  <img src="https://img.shields.io/badge/Language-HTML-orange?style=for-the-badge&logo=html5" alt="HTML">
  <img src="https://img.shields.io/badge/Language-CSS-blue?style=for-the-badge&logo=css3" alt="CSS">
</p>







<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a>
    <img src="/static/frog.png" alt="Logo" width="400" height="300">
  </a>

  

  <p align="justify">The Chat-GPT3-Bot is a simple chat bot designed to generate course descriptions based on a given course title and subject. It utilizes the GPT-3 API from OpenAI and the Flask web framework to provide this functionality. By inputting a course title and subject, the Chat-GPT3-Bot will generate a course description that is based on the given input. This description may include details such as the course goals, topics covered, and intended audience, among others. The Chat-GPT3-Bot is a useful tool for quickly generating descriptions for courses, and it is simple to use with just a few input fields and a button to generate the description. </p>
  
  [live demo](https://samuelaboye.pythonanywhere.com/)
  
  # Requirements
  - Flask
  - OpenAI API key
  
  # Setup
  1. Clone this repository and navigate to the project directory:
  
  ```ruby
  git clone https://github.com/saboye/Chat-GPT3-Bot.git
  
  cd Chat-GPT3-Bot
  ```
  
  
  2. Create a virtual environment and install the required packages:
  
  ```ruby
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  
  ```
  
  3. Set your OpenAI API key as an environment variable:
  
  
  ```ruby
  export OPENAI_API_KEY=your_api_key
  ```
  
  4. Run the app:
  
  ```ruby
  flask run
  ```
  
  # Usage
  
  1. Navigate to http://localhost:5000 in your web browser.
  2. Enter a course title and subject in the input fields and click "Generate Description".
  3. The generated course description will be displayed below the input fields.

# Note
<p align="justify"> This is just a sample project and the generated course descriptions may not always be accurate or complete. Use at your own risk! </p>
 


