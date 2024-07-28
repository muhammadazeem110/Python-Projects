# **Introducing the Mail Merge Challenge**

## **Introduction**
This project demonstrates how to automate sending emails to multiple recipients using the Mail Merge technique. The code is written in Python and leverages libraries such as smtplib for sending emails and python-docx for handling .docx files.

## **Prerequisites**
Before running the script, ensure you have the following:
- Python installed on your machine.
- An email account to send emails from (Gmail is used in this example).
- A .docx file containing the email template.
- A .txt file containing the recipients' names.
## **Installation**
1) Clone the Repository:
```bash
git clone https://github.com/yourusername/mail-merge-automation.git
cd mail-merge-automation
```
2) Install Required Packages:
```bash
pip install -r requirements.txt
```

## **Configuration**
1) **Recipients File:**
Create a text file named names.txt with each recipient's name on a new line:
```bash
John Doe
Jane Smith etc.
```
2) **Email Template:**

Create a .docx file named email_template.docx containing your email template. Use placeholders for dynamic content, such as {Name} for the recipient's name.
## **Conclusion**
This project provides a simple yet effective way to send personalized emails to multiple recipients using a mail merge technique in Python with .docx and .txt files. You can customize the email template and recipient list to fit your specific needs.
## **Documentation 📚**
For more information on Python basics, refer to the [official Python documentation](https://docs.python.org/3/).

## **Credits 👏**
This project is inspired by Angela's "[100 Days of Python](https://www.udemy.com/course/100-days-of-code/?couponCode=LETSLEARNNOWPP)" course.

## **License 📄**
This project is licensed under the [MIT License](https://github.com/muhammadazeem110/Python-Projects/blob/main/LICENSE).
