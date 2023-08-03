import requests
import pyfiglet as pyfiglet
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("Email - BREACH")
print(ascii_banner)
print("                                                  "   + "by Eswar H4ck3r" + "\n")

print("-" * 60)
print(str(datetime.now()))
print("-" * 60)


def load_breached_emails(filename):
    with open(filename, "r") as file:
        return set(line.strip() for line in file)

def is_email_breached(email, breached_emails):
    return email in breached_emails

def main():
    breached_emails_file = "breached_emails.txt"
    breached_emails = load_breached_emails(breached_emails_file)

    user_email = input("Enter your email address: ")
    if is_email_breached(user_email, breached_emails):
        print(f"WARNING: The email '{user_email}' has been breached!")
    else:
        print(f"The email '{user_email}' is not found in the breached list. It is safe.")

if __name__ == "__main__":
    main()
