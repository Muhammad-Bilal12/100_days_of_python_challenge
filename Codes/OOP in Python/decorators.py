# Decorator is used to modified the Function


def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks")
    return mfx


@greet
def hello():
    print("Hello World")

# this is something like this
# greet(hello())


# hello()


# If we create a argument type funtion
@greet
def add(a, b):
    print(a + b)


add(4, 5)
