#   Questionaire 1: Ask Directly
#   Questionaire 2: Use Generic Algorithm to calculate % rate of Risk



def risk_tolerance_level():
    risk_tolerance_level = float(input("Please provide your Risk Tolerance Level Rate (1-5)\n"))
# 1-Min    2-Low    3-Medium    4-High    5-Max
    return risk_tolerance_level

print(risk_tolerance_level())