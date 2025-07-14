def outer():
    x=68
    def inner():
        print("value of s is inside inner:", x)
    inner()
outer()