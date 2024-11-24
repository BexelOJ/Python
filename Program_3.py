# Total no. of countries without repetition
if __name__ == '__main__':
    N = int(input())
    country = set()
    for _ in range(N):
        country.add(input())
    print(len(country))