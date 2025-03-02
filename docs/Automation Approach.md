# Approach to Automating Login Functionality

## **1. Understanding the Login Functionality**
The login functionality is a critical feature that allows users to authenticate and access the application securely. It consists of:
- **Username/Email field**
- **Password field (masked)**
- **Login Button**
- Optional: "Remember Me" checkbox, "Forgot Password" link

---

## **2. Tools and Technologies Used**
For effective automation, the following tools were chosen:
- **Programming Language**: Python
- **Test Automation Framework**: Selenium WebDriver
- **Test Runner**: pytest
- **Browser**: Chrome (via ChromeDriver)
- **Reporting Tool**: pytest-html
- **Test File**: .\tests\

---

## **3. Test Scenarios for Automation**
### **Positive Test Case**
1. **Valid Login**

### **Negative Test Cases**
2. **Invalid Username & Valid Password**
3. **Valid Username & Invalid Password**
4. **Invalid Username & Invalid Password**
5. **Empty Username & Password**
6. **Password Masking Verification**
7. **Forgot Password Link Redirection**
8. **Logout Functionality**

---

## **4. Steps to Automate Login Tests**
### **Step 1: Setup WebDriver**
- Initialize ChromeDriver and set implicit waits.
- Open the login page.

### **Step 2: Locate Web Elements**
- Identify elements using ID, Classname,CSS Selectors or XPath.

### **Step 3: Perform Actions**
- Input credentials and click login.

### **Step 4: Validate Expected Behavior**
- Verify login success/failure using assertions.

### **Step 5: Generate Test Reports**
- Use pytest-html to document test results.

---

## **5. Conclusion**
Automating login functionality enhances test coverage, accuracy, and efficiency. The structured test automation approach ensures maintainability and scalability.
