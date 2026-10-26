from flask import Flask, render_template, request, redirect, url_for
import urllib.parse
from data import SUBJECTS # Import the data we just created

app = Flask(__name__)

PRICES = {
    "NSSCO": {"single": 30, "bundles": {3: 80, 5: 130, 10: 250}},
    "NSSCAS": {"single": 20, "bundles": {3: 50, 5: 80, 10: 150}}
}

WHATSAPP_NUMBER = "264818412379"

@app.route("/")
def index():
    # Pass the dictionary keys to the template
    return render_template("index.html", prices=PRICES, syllabus_data=SUBJECTS)

@app.route("/checkout", methods=["POST"])
def checkout():
    syllabus = request.form.get("syllabus")
    year = request.form.get("year")
    delivery = request.form.get("delivery")
    
    # Get all selected subjects
    selected_subjects = request.form.getlist("subject") 
    # Get all selected papers (format: "Subject_Name|Paper_1")
    selected_papers = request.form.getlist("paper")
    
    # Group the papers by subject
    subject_papers = {}
    for item in selected_papers:
        subj, paper = item.split("|")
        if subj not in subject_papers:
            subject_papers[subj] = []
        subject_papers[subj].append(paper)

    subject_count = len(subject_papers)
    
    # Calculate price based on the number of subjects selected
    price = 0
    if syllabus in PRICES:
        bundles = PRICES[syllabus]["bundles"]
        if subject_count >= 10 and 10 in bundles:
            price = bundles[10]
        elif subject_count >= 5 and 5 in bundles:
            price = bundles[5]
        elif subject_count >= 3 and 3 in bundles:
            price = bundles[3]
        else:
            price = subject_count * PRICES[syllabus]["single"]

    # Format the message for WhatsApp
    subject_lines = []
    for subj, papers in subject_papers.items():
        subject_lines.append(f"  - {subj} ({', '.join(papers)})")
        
    subjects_text = "\n".join(subject_lines)

    message = (
        f"Hello! I would like to order past papers.\n\n"
        f"*Syllabus:* {syllabus}\n"
        f"*Year:* {year}\n"
        f"*Delivery:* {delivery}\n\n"
        f"*My Subjects:*\n{subjects_text}\n\n"
        f"*Estimated Total:* N${price}\n\n"
        f"Please confirm my order."
    )
    
    encoded_message = urllib.parse.quote(message)
    whatsapp_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={encoded_message}"
    
    return redirect(whatsapp_url)

if __name__ == "__main__":
    app.run(debug=True, port=5002)