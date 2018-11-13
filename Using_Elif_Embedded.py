score = input("Enter Score: ")
answer = float(score)
if 0.0 <= answer <= 1.0:
	if answer >= 0.9:
		print("A")
	elif answer >= 0.8:
		print("B")
	elif answer >= 0.7:
		print("C")
	elif answer >= 0.6:
		print("D")
	elif answer < 0.6:
		print("F")
else:
	print("Please Enter a Number between 0.0 and 1.0")
