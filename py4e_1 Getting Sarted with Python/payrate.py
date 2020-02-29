def computepay(h,r):
    if h > 40:
        oth = h - 40
        otr = r * 1.5
        return ((40 * r) + (oth * otr))
    else:
        return (h * r)

hrs = input("Enter Hours:")
fhrs = float(hrs)
rate = input("Enter Pay Rate:")
frate = float(rate)

p = computepay(fhrs, frate)
print(p)
