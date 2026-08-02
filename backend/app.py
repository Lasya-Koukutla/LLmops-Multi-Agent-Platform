from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai
import os
import time

# Import AI Agents
from agents.validator import validate_prompt
from agents.analyzer import analyze_prompt
from agents.refiner import refine_prompt
from agents.responder import generate_response

# Import Logger
from logs.logger import save_log

# Load Environment Variables
load_dotenv()

# Create Flask App
app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

# Create Gemini Client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    try:

        start_time = time.time()

        # Get user prompt
        data = request.get_json()
        prompt = data.get("prompt", "")

        # -----------------------------
        # Agent 1 : Validator
        # -----------------------------
        is_valid, validation_message = validate_prompt(prompt)

        if not is_valid:
            return jsonify({
                "validation": validation_message,
                "response": validation_message
            })

        # -----------------------------
        # Agent 2 : Analyzer
        # -----------------------------
        analysis = analyze_prompt(prompt)

        # -----------------------------
        # Agent 3 : Refiner
        # -----------------------------
        refined_prompt = refine_prompt(prompt)

        # -----------------------------
        # Agent 4 : Responder
        # -----------------------------
        answer = generate_response(client, refined_prompt)

        # Calculate execution time
        execution_time = round(time.time() - start_time, 2)

        # Save Log
        save_log(
            prompt=prompt,
            analysis=analysis,
            refined_prompt=refined_prompt,
            response=answer,
            execution_time=execution_time
        )

        return jsonify({
            "validation": validation_message,
            "analysis": analysis,
            "refined_prompt": refined_prompt,
            "response": answer,
            "execution_time": f"{execution_time} seconds"
        })

    except Exception as e:

       print("Error:", e)

    return jsonify({
        "validation": "Failed",
        "analysis": "",
        "refined_prompt": "",
        "execution_time": "",
        "response": "Unable to connect to Gemini API. Please try again later."
    }), 500

if __name__ == "__main__":
    app.run(debug=True)