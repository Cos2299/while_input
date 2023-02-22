start_n = float(input("Enter the starting value: "))
end_n   = float(input("Enter the ending value: "))

if start_n <= end_n:
   n = start_n
   while n <= end_n:
       print(n)
       n += 1
else:
    n = start_n
    while n >= end_n:
        print(n)
        n -= 1