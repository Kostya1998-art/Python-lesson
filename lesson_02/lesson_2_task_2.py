def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


result = is_year_leap(2021)
print(f'Год 2021: {result}')
