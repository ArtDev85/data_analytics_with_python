def age_group_label(age, young=30, senior=60):
    if age < young:
        return "Young"
    elif age < senior:
        return "Middle"
    else:
        return "Senior"


def income_band(income, low=30000, high=70000):
     
    if income < low:
        return "Low income"
    elif income < high:
        return "Middle income"
    else:
        return "High income"
    