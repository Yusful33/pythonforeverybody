def computepay(hours,rate):
    print("In Computepay", hours, rate)
    if hours > 40:
        reg = hours * rate
        overtime = (hours - 40.0) * (rate * 0.5)
        expectedpay = reg + overtime
    else:
        expectedpay = hours * rate
    return expectedpay
Q1 = input("Entire Hours: ")
Q2 = input("Entire Rate: ")
FQ1 = float(Q1)
FQ2 = float(Q2)
# print(FQ1, FQ2)
paycheck = computepay(FQ1,FQ2)
print("Pay:",paycheck)
