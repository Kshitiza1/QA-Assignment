## Summary of the Project
This project automates:
- **Web UI Testing**: Login, Forgot Password, Logout flows using Selenium & PyTest.
- **API Testing**: Validation of endpoints for creating, retrieving, updating, and deleting video game records using Postman & Newman.
- **Performance Testing**: Evaluating API response times using JMeter.

The automation covers **positive and negative test cases**, ensuring robustness and reliability.

---

## Test Execution Results

### 🔹 Web Automation Results
![task1-report-html.png](..%2Fimages%2Ftask1-report-html.png)

### 🔹 API Testing Results
![Postman-result-1.png](..%2Fimages%2FPostman-result-1.png)
![Postman-result-2.png](..%2Fimages%2FPostman-result-2.png)

### 🔹 JMeter Performance Report
![img.png](..%2Fimages%2Fimg.png)

---

## Test Cases Included

### 1. Web UI Test Cases (Selenium + PyTest)
 **Login Tests**  
- Valid login with correct credentials  
- Invalid login (wrong password, wrong username, wrong credentials)  
- Empty username and password validation  

 **Forgot Password Tests**  
- Verify password reset flow   

 **Logout Tests**  
- Successful logout functionality

---

### 🔗 2. API Test Cases (Postman)
 **Retrieve All Video Games (GET)**
- Add a new game with all required fields  
- Verify status code, array response, response data, time and content-type  

**Create A Video Game (POST)**
- Add a new game with all required fields  
- Negative test: Try sending incomplete data while creating a game

 **Retrieve Video Game (GET)**
- Fetch an existing game by ID  
- Negative test: Try fetching a non-existing game

**Update Video Game (PUT)**
- Modify an existing game’s details  
- Negative test: Update with invalid data, fetch non-existing game 

**Delete Video Game (DELETE)**
- Successfully remove a game  
- Negative test: Deleting a non-existing ID  

---

### 3. Performance Test Cases (JMeter)
**Response Time Analysis**  
- Test API delay between **1-10 seconds**  
- Check if API responses meet the **expected threshold**  
- Measure **throughput and request handling under load**  
