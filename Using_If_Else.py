hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
if h > 40:
    reg = h * r
    overtime = (h - 40.0) * (r * 0.5)
    pay = reg + overtime
else:
    pay = reg
print("Overtime:", pay)
