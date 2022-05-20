from django.test import TestCase

# import datetime

# current_year = datetime.datetime.now().year
# # print("current year", current_year)

# start_year = current_year - 9

# # print("start year", start_year)




# def get_vacation_days(start_year, current_year):
#     vacation_days = 0
#     work_year = current_year - (start_year + 1)
#     if work_year <= 3:
#         vacation_days = 18
#     if work_year >= 4 and work_year <= 7:
#         vacation_days = 24
#     if work_year >= 8 and work_year <= 10:
#         vacation_days = 28
#     if work_year > 10:
#         vacation_days = 30
#     return vacation_days


print(get_vacation_days(start_year, current_year))


