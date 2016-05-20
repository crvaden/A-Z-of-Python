

# nonlocal variables

x = "Joe Williams"


def first_name():
    x = "Bob"
    print(x)

    def second_name():
        nonlocal x
        x += " Smith"
        print(x)
    second_name()

first_name()
print(x)

