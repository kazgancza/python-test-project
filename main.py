print("Hello GitHub!")

for i in range(0,100):
    print(i)

def is_prime(number):
    for i in range(2,number):
        if number % i == 0 and i != number:
            return False
    return True

    

print(is_prime(7))
print(is_prime(6))
