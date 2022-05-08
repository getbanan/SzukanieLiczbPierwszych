def isPrime(i):
    for n in range(2, i):
        if (i % n) == 0:
            return False
    return True

def main():
    print("Podaj ilość liczb pierwszych:")
    n = int(input())
    i = 2
    while True:
        if n > 0:
            if isPrime(i):
                print(i)
                n -= 1
                i += 1
            else:
                i += 1

main()