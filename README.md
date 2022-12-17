# Overview
This automated framework includes 6 test cases that tests the whole UI and validates the API endpoints to make sure it is matching what needs to populate within the UI.

Additional 3 manual test cases are attached separately together with the Bug Reports.
The video recording of the automated test running is attached within the same zip file. Together with some screenshots of bugs / defects. In addition, I have included the video recording of execution of the manual test cases.

Each file within the Automated Framework includes comments about what each part is responsible for.

## Instructions to Run the Automated Tests

1. Clone or download/copy this framework into your local machine.
2. Open a Python editor and open the folder that contains the framework within it.
3. Navigate to the conftest.py file and replace the chrome and firefox driver's directory accordingly based on where it is stored on your local machine.
4. Run the Dashboard locally on your machine.
5. Clone or download/copy the dashboard from https://github.com/syndio/qa-interview-dashboard into your local machine.
6. Open terminal, navigate to where the dashboard contents are located.
7. Enter "npm install" to install the node modules for the dashboard.
8. Enter "npm start" to start the dashboard locally on your machine.
9. Once the Dashboard is up and running, as long as the url of the dashboard is ("http://localhost:3000/"), tests are ready to run.
10. To run the tests, navigate through the terminal to where the framework is stored; Then, type in "pytest" and all test cases will get executed.
11. Additionally, if your Editor allows to run the test cases on the Editor itself, locate the test_e2e.py file within the tests package and run it.
12. Keep in mind, the framework utilizes selenium synchronization; Tests will run within seconds.

## Test Case Execution Status

* Test cases TC1, TC5 will pass based on the Dashboard's abilities
* Test cases TC2, TC3, and TC4 will fail due to bugs and not developed UI
* Test case TC6 will fail due to the window title of the web page being "React App";

## Manual Test Cases and Bug Report

Manual test cases and the bug report is attached separately within a zip file.

Extract the zip file and access the test cases and the bug report through Excel. Within the zip file, there are 4 folders which includes videos of test execution, a copy of the automated framework, screenshots, and the test cases with the bug reports.