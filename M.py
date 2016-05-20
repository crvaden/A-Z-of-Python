

# Module Names

def print_evens():
    print('Printing all even numbers up to 100')
    for i in range(101):
        if i % 2 == 0:
            print(i)


def print_odds():
    print('Printing all odd numbers up to 100')
    for i in range(101):
        if i % 2 != 0:
            print(i)

if __name__ == '__main__':
    choice = input('odds/evens: ')

    if choice == 'odds':
        print_odds()
    elif choice == 'evens':
        print_evens()


