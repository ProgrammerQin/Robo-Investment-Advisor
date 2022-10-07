#   Output Example:
#   Medium Level Risk investor
#   % [List of Medium Level Mutual Funds]
#   % [List of Medium Level Stocks]

#   % is fixed number hard coded based on Industry standard
#   For stocks, I will use historical rate of return to give suggestions.

#   calculate rate of return from the suggested package and compare with user expectation

risk_tolerance_level = 3

if risk_tolerance_level == 0:
    Stock_ratio = 10
    Digital_currency_ratio = 10
    Foreign_currency_ratio = 80

if risk_tolerance_level == 1:
    Stock_ratio = 20
    Digital_currency_ratio = 20
    Foreign_currency_ratio = 60

if risk_tolerance_level == 2:
    Stock_ratio = 30
    Digital_currency_ratio = 30
    Foreign_currency_ratio = 40

if risk_tolerance_level == 3:
    Stock_ratio = 30
    Digital_currency_ratio = 40
    Foreign_currency_ratio = 30

if risk_tolerance_level == 4:
    Stock_ratio = 30
    Digital_currency_ratio = 50
    Foreign_currency_ratio = 20

if risk_tolerance_level == 5:
    Stock_ratio = 40
    Digital_currency_ratio = 50
    Foreign_currency_ratio = 10

investment_info = Stock_ratio, "Stock", Digital_currency_ratio, "DC", Foreign_currency_ratio, "FC"

print(str(investment_info))