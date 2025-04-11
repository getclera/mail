from flask import Flask, render_template, request, jsonify
import os
import json
from generate_email import generate_email

app = Flask(__name__)

@app.route('/')
def landing():
    """Serve the landing page"""
    return render_template('landing.html')

@app.route('/generator')
def generator():
    """Serve the email generator page"""
    return render_template('index.html')

@app.route('/api/generate-email', methods=['POST'])
def api_generate_email():
    """API endpoint to generate an email based on provided parameters"""
    data = request.get_json()
    
    recipient_name = data.get('recipient_name')
    previous_company = data.get('previous_company')
    previous_role = data.get('previous_role')
    current_salary = data.get('current_salary')
    
    if current_salary and current_salary.isdigit():
        current_salary = int(current_salary)
    else:
        current_salary = None
    
    # Generate the email text
    email_text = generate_email(
        recipient_name=recipient_name,
        previous_company=previous_company,
        previous_role=previous_role,
        current_salary=current_salary
    )
    
    return jsonify({'email': email_text})

@app.route('/api/stats', methods=['GET'])
def api_stats():
    """API endpoint to get usage statistics"""
    # In a real application, this would track and return actual usage stats
    stats = {
        'emails_generated': 1234,
        'pull_requests': 87,
        'most_effective_template': 'salary_focus',
        'avg_response_rate': '23%'
    }
    return jsonify(stats)

@app.route('/contribute')
def contribute():
    """Serve the contribution page"""
    return render_template('index.html', contribute=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True) 