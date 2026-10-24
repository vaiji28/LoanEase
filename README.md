\# LoanEase — Loan Management System



LoanEase is a Django-based web application for managing loan applications.



\## Features

\- Loan application form with validation

\- Automatic application ID generation

\- EMI calculation

\- Loan status tracking

\- Employee login and dashboard

\- Approve or reject loan applications

\- Django admin integration



\## Technologies Used

\- Python

\- Django

\- HTML

\- CSS

\- SQLite for local development



\## Run Locally



1\. Clone the repository.

2\. Create and activate a Python virtual environment.

3\. Install dependencies:



&#x20;  `pip install -r requirements.txt`



4\. Create a `.env` file with your own configuration:



&#x20;  `DJANGO\_SECRET\_KEY=your-secret-key`



&#x20;  `DJANGO\_DEBUG=True`



&#x20;  `DJANGO\_ALLOWED\_HOSTS=127.0.0.1,localhost`



&#x20;  `EMPLOYEE\_USERNAME=your-username`



&#x20;  `EMPLOYEE\_PASSWORD=your-password`



5\. Run database migrations:



&#x20;  `python manage.py migrate`



6\. Start the development server:



&#x20;  `python manage.py runserver`



7\. Open `http://127.0.0.1:8000/` in your browser.



\## Security Note

Never commit `.env`, database files, passwords, or secret keys to GitHub.

