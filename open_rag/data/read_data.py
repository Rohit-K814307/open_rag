import pandas as pd
import re

class DataSet():

    def __init__(self, path_to_csv, myemail, num_emails_data):
        self.path_to_csv = path_to_csv
        self.df = pd.read_csv(self.path_to_csv)
        self.subjects = self.df["Subject"]
        self.body = self.df["Body"]
        self.myemail = myemail

        self.emails = []
        self.email_join()
        self.check_sizes(num_emails_data)
        

    def check_sizes(self, size):
        if len(self.emails) > size:
            print(f"Initializing RAG data with {size} emails...")
            self.emails = self.emails[len(self.emails)-size::]
        else:
            self.check_sizes(size-1)
        


    def clean_text(self, text):
        # Remove email headers and footers (adapt patterns as needed)
        text = re.sub(r"^.*On [A-Za-z]{3}, [A-Za-z]{3} \d{1,2}, \d{4} at \d{2}:\d{2} .*\r?\n", "", text, flags=re.MULTILINE)
        text = re.sub(r"--.*\r?\n", "", text, flags=re.MULTILINE)
        text = re.sub(r"Sincerely,\s+.*\r?\n", "", text, flags=re.MULTILINE)
        text = re.sub(r"Thank you,\s+.*\r?\n", "", text, flags=re.MULTILINE)

        # Combine whitespaces and remove extra newlines
        text = re.sub(r"\s+", " ", text)
        text = re.sub(r"\n+", "\n", text)

        # Define blacklist (modify as needed)
        blacklist = []

        # Remove special characters (modify the pattern for your needs)
        text = re.sub(r"[^\w\s\d\-+\.]", "", text)  # Removes most punctuation and special characters

        # Remove blacklisted words
        words = text.split()
        cleaned_words = [word for word in words if word.lower() not in blacklist]

        return " ".join(cleaned_words)

    def email_join(self):

        fwdtext = "fwd"

        for i in range(len(self.subjects)):
            if str(self.myemail) not in str(self.df["To: (Address)"][i].lower()):
                subj = str(self.df["Subject"][i]).lower()

                if fwdtext.lower() in subj:
                    pass

                else:
                    email = self.clean_text(str(self.df["Body"][i]))
                    if len(email) > 150 and len(email) <= 512:
                        self.emails.append(email)