import re
def find_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    matches = re.findall(email_pattern, text)

    return matches
sample_text = "Contact us at info@example.com or support@company.com for assistance."

email_addresses = find_emails(sample_text)
print("Email Addresses Found:")
print(email_addresses)
