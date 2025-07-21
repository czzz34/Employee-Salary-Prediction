from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load your trained model
model = joblib.load("best_model.pkl")

# All dropdown options must match exactly how you encoded them during training
options = {
    "job_title": [
        "Analyst", "Architect", "Consultant", "Engineer", "Manager",
        "Research", "Scientist", "Other"
    ],
    "experience_level": ["Entry-level", "Mid-level", "Senior", "Executive"],
    "employment_type": ["FT", "PT", "CT", "FL"],
    "company_location": ["Asia", "Europe", "America", "Other"],
    "company_size": ["S", "M", "L"],
    "remote_ratio": [0, 50, 100],
    "education_required": [
        "No degree", "Associate", "Bachelor’s", "Master’s", "PhD"
    ],
    "years_experience": [str(i) for i in range(0, 20)],  # "0" through "19"
    "industry": [
        "Automotive", "Consulting", "Technology", "Real Estate", "Government",
        "Healthcare", "Telecommunications", "Finance", "Transportation", "Energy","Gaming","Manufacturing","Education"
    ]
}

def encode_input(form):
    """
    Build the feature vector in the exact same order
    your model was trained on:
      [job_title, experience_level, employment_type,
       company_location, company_size, remote_ratio,
       education_required, years_experience, industry]
    """
    return [
        options["job_title"].index(form["job_title"]),
        options["experience_level"].index(form["experience_level"]),
        options["employment_type"].index(form["employment_type"]),
        options["company_location"].index(form["company_location"]),
        options["company_size"].index(form["company_size"]),
        options["remote_ratio"].index(int(form["remote_ratio"])),
        options["education_required"].index(form["education_required"]),
        int(form["years_experience"]),                                # numeric
        options["industry"].index(form["industry"])
    ]

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        features = encode_input(request.form)
        prediction = model.predict([features])[0]
    return render_template("index.html",
                           options=options,
                           prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
