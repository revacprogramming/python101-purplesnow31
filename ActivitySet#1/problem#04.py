# Conditional Execution

hrs = input("Enter hours? ")
rate=input("Enter Rate:")
r = float(rate)
if h <= 40:
    print(h*r)
elif h > 40:
    print(40 * r + (h - 40)*1.5*r)