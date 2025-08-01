def double_number(n):
    return n * 2

numbers = [2, 4, 6, 8, 10]

doubled_numbers = map(double_number, numbers)

print("اصل نمبرز:", numbers)
print("دوگنے نمبرز:", list(doubled_numbers))