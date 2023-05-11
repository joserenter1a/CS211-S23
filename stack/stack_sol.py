from collections import deque as stack  # import double ended queue, to use as a stack


# we do not need to create our own stack implementation, we can simply use the one supported by Python


def reverse_string(string: str):
    st = stack()
    print(st)
    for char in string:  # every char in our string
        st.append(char)  # push the char onto the stack
    print(st)
    reversed_string = ""  # create an empty reverse string
    while st:  # could also do len(st) != 0
        print(st)
        reversed_string += st.pop()  # pop returns whatever is on the top of the stack,
        # accumulation to an empty string ^

    return reversed_string  # return new string



