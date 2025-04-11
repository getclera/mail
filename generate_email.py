#!/usr/bin/env python3

def generate_email(recipient_name, previous_company, previous_role, current_salary=None):
    """
    Generate a creative outreach email for talented engineers.
    
    Args:
        recipient_name (str): The name of the recipient
        previous_company (str): The engineer's previous company
        previous_role (str): The engineer's previous role
        current_salary (int, optional): The engineer's current salary
    
    Returns:
        str: The generated email text
    """
    
    new_job = upgrade_job(current_salary)
    
    email_text = f"""
Subject: {recipient_name}, Your Engineering Talents Are Being Underutilized

Hey {recipient_name}!

I noticed your impressive {previous_role} background at {previous_company}.

Did you know that engineers with your experience are earning significantly more elsewhere?

{new_job['message']}

Next steps:
1. {new_job['step1']}
2. {new_job['step2']}

Let's chat about your future,
The Clera Team

P.S. Want to improve this email? Open a PR on github.com/clera/outreach-emails
"""
    
    return email_text.strip()


def upgrade_job(current_salary=None):
    """
    Generate upgraded job details based on current salary.
    
    Args:
        current_salary (int, optional): The current salary
        
    Returns:
        dict: Information about the potential new position
    """
    result = {
        'message': "We're connecting engineers like you with elite opportunities that match your worth.",
        'step1': "Reply with your preferred location (remote options available)",
        'step2': "Join a conversation about your fit with a start-up with strong engineering culture"
    }
    
    if current_salary:
        new_salary = current_salary + 20000
        result['message'] = f"We have opportunities starting at ${new_salary:,} for someone with your skills."
    
    return result


if __name__ == "__main__":
    # Example usage
    name = "Daniel"
    old_job = "Product Engineering"
    old_company = "Airbnb"
    
    # Without salary info
    print(generate_email(name, old_company, old_job))
    print("\n" + "-"*50 + "\n")
    
    # With salary info
    print(generate_email(name, old_company, old_job, 150000)) 