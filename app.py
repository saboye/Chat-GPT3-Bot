import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        course_title = request.form["course_title"]
        course_subject = request.form["course_subject"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(course_title, course_subject),
            temperature=0.9,
            max_tokens=50,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
          
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(course_title, course_subject):
    return """Generate a course description for a {} course on {}'""".format(course_title, course_subject
    )
    

if __name__=='__main__':
    app.run()
