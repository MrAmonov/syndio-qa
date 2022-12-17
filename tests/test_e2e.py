from pageObjects.Dashboard import Dashboard
from utilities.BaseClass import BaseClass
import requests
import json

# End-to-end testing of the Dashboard with integration of API endpoints to verify the data

# Test Case 1 and 5 will Pass
# Test Case 2, 3, and 4 will Fail due to Bugs on the UI or the web not being fully developed yet
# Test Case 6 will fail due to the Title of the window being "React App" instead of Syndio/Dashboard as per requirements


class TestE2E(BaseClass):
    # This test case tests and checks for Gender and details based on the API under the Group by Function tab
    def test_tc1(self):
        dash = Dashboard(self.driver)
        dash.get_gender().click()
        pay = dash.get_pay_equity_gap().text
        pay = pay.strip('¢')
        # The API request below gets pulled to check and validate what has to show on the web UI
        r = requests.get("https://run.mocky.io/v3/a9f6a4b7-d03c-4a45-b64b-791e054f36b8")
        rs = r.json()
        ra = json.dumps(rs["data"]["gender"]["payEquityGap"]["data"]["minority"]["value"])
        ra = ra.strip('\"')
        ra = ra.strip('\\\\u00a2')
        assert pay == ra, "Assertion Failed for Gender under Function"
        employees = dash.get_employees().text
        ri = json.dumps(rs["data"]["gender"]["employeeComparison"]["data"]["value"])
        ri = ri.strip('\"')
        assert employees == ri, "Assertion Failed for Gender under Function"
        budget = dash.get_budget().text
        rb = json.dumps(rs["data"]["gender"]["budget"]["data"]["value"])
        rb = rb.strip('\"')
        assert budget == rb, "Assertion Failed for Gender under Function"

    # This test case tests and checks for Race and details based on the API under the Group by Function tab
    def test_tc2(self):
        dash = Dashboard(self.driver)
        dash.get_race().click()
        pay = dash.get_pay_equity_gap().text
        pay = pay.strip('¢')
        # The API request below gets pulled to check and validate what has to show on the web UI
        r = requests.get("https://run.mocky.io/v3/a9f6a4b7-d03c-4a45-b64b-791e054f36b8")
        rs = r.json()
        ra = json.dumps(rs["data"]["race"]["payEquityGap"]["data"]["minority"]["value"])
        ra = ra.strip('\"')
        ra = ra.strip('\\\\u00a2')
        assert pay == ra, "Assertion Failed for Race under Function"
        employees = dash.get_employees().text
        ri = json.dumps(rs["data"]["race"]["employeeComparison"]["data"]["value"])
        ri = ri.strip('\"')
        assert employees == ri, "Assertion Failed for Race under Function"
        budget = dash.get_budget().text
        rb = json.dumps(rs["data"]["race"]["budget"]["data"]["value"])
        rb = rb.strip('\"')
        assert budget == rb, "Assertion Failed for Race under Function"

    # This test case tests and checks for Gender and details based on the API under the Group by Role tab
    def test_tc3(self):
        dash = Dashboard(self.driver)
        dash.get_gender().click()
        pay = dash.get_pay_equity_gap().text
        pay = pay.strip('¢')
        # The API request below gets pulled to check and validate what has to show on the web UI
        r = requests.get("https://run.mocky.io/v3/f1b01b57-3147-476a-a632-0c10ad2a3c1a")
        rs = r.json()
        ra = json.dumps(rs["data"]["gender"]["payEquityGap"]["data"]["minority"]["value"])
        ra = ra.strip('\"')
        ra = ra.strip('\\\\u00a2')
        assert pay == ra, "Assertion Failed for Gender under Role"
        employees = dash.get_employees().text
        ri = json.dumps(rs["data"]["gender"]["employeeComparison"]["data"]["value"])
        ri = ri.strip('\"')
        assert employees == ri, "Assertion Failed for Gender under Role"
        budget = dash.get_budget().text
        rb = json.dumps(rs["data"]["gender"]["budget"]["data"]["value"])
        rb = rb.strip('\"')
        assert budget == rb, "Assertion Failed for Gender under Role"

    # This test case tests and checks for Race and details based on the API under the Group by Role tab
    def test_tc4(self):
        dash = Dashboard(self.driver)
        dash.get_race().click()
        pay = dash.get_pay_equity_gap().text
        pay = pay.strip('¢')
        # The API request below gets pulled to check and validate what has to show on the web UI
        r = requests.get("https://run.mocky.io/v3/f1b01b57-3147-476a-a632-0c10ad2a3c1a")
        rs = r.json()
        ra = json.dumps(rs["data"]["race"]["payEquityGap"]["data"]["minority"]["value"])
        ra = ra.strip('\"')
        ra = ra.strip('\\\\u00a2')
        assert pay == ra, "Assertion Failed for Race under Role"
        employees = dash.get_employees().text
        ri = json.dumps(rs["data"]["race"]["employeeComparison"]["data"]["value"])
        ri = ri.strip('\"')
        assert employees == ri, "Assertion Failed for Race under Role"
        budget = dash.get_budget().text
        rb = json.dumps(rs["data"]["race"]["budget"]["data"]["value"])
        rb = rb.strip('\"')
        assert budget == rb, "Assertion Failed for Race under Role"

    # This test case checks for the dropdown and different options that exists with the API integration for dropdown
    def test_tc5(self):
        dash = Dashboard(self.driver)
        dash.get_dropdown().click()
        dash_change = dash.get_dropdown_change().text
        assert dash_change == "CHANGE GROUP", "Assertion Failed to Verify the Dashboard Name"
        function = dash.get_function().text
        # The API request below gets pulled to check and validate what has to show on the web UI
        r = requests.get("https://run.mocky.io/v3/9e343425-c47c-4c7f-a1ac-972c099be0ed")
        rs = r.json()
        ra = json.dumps(rs[0]["label"])
        ra = ra.strip('\"')
        assert function == ra, "Assertion Failed for Group by Function tab"
        role = dash.get_role().text
        ri = json.dumps(rs[1]["label"])
        ri = ri.strip('\"')
        assert role == ri, "Assertion Failed for Group by Role tab"

    # This test case checks for the title name of the given Dashboard's window
    def test_tc6(self):
        title_of_window = self.driver.title
        assert title_of_window == "Dashboard", "Assertion Failed, Title does not match"
    