# QA Assignment - Automation & Performance Testing

## Overview

This project includes web automation testing, API testing with Postman, and performance testing with JMeter. The repository contains test scripts, reports, and setup instructions to help you execute the tests successfully.

___

## How to Run the Project

The project consists of three main parts:

1. Web Automation Testing (Selenium + Python + PyTest)

2. API Testing (Postman + Newman)

3. Performance Testing (JMeter)

Below are the step-by-step instructions to set up and execute the tests.

___

## Web Automation Testing (Selenium & PyTest)

### Dependencies
- Python (>= 3.8)
- Selenium WebDriver
- PyTest
- WebDriver Manager

### Installation Steps

1. Clone the Repository
```
git clone https://github.com/yourusername/repo-name.git
cd repo-name
```
2. Create a Virtual Environment
```
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```
3. Install Dependencies
```
pip install -r requirements.txt
```

4. Run the Tests
```
pytest tests/login.py -v   # Run login test cases
pytest tests/forgotpassword.py -v   # Run forgot password cases
pytest tests/logout.py -v   # Run logout test cases
pytest .\tests\login.py --html=reports/task1_report.html --self-contained-html #Run and generate reports
pytest .\tests\login.py -m task2 --html=reports/task2_report.html --self-contained-html -v #Run only cases with mark task2
```

---

## API Testing (Postman)

### Dependencies

Postman (GUI for API testing)

### Running API Tests in Postman

1. Import Postman Collection

    - Open Postman → Click Import → Upload the .json collection file.

2. Set Environment Variables (if required)

    - Go to Environments → Add API base_url, auth_token, etc.

3. Run Collection

    - Click Runner → Select the collection → Click Run.

---

## Performance Testing (JMeter)

### Dependencies

- Apache JMeter

### Running JMeter Tests
- Open JMeter
```
jmeter
```

- Load the JMX File
    - Open JMeter UI → Click File → Open → Select httpbintest.jmx
  
- Run the Test Plan
  - Click the Start (▶) button to execute the test.

- Generate HTML Report through Non-GUI
```
jmeter -n -t httpbintest.jmx -l results.csv -e -o ReportFolder
```

- View Report

Open ReportFolder/index.html in a browser.

---

## Additional Documentation: 
For theory and detailed reports, visit the [`docs/`](docs/) folder.

---
## Conclusion

This repository contains automated test scripts for web UI, APIs, and performance testing. Follow the above steps to set up, run tests, and generate reports.
