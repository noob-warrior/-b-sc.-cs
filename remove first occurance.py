def x(s, c) :
    counts = s.count(c)
    s = list(s)
    while counts :
        s.remove(c)
        counts -= 1
    s = '' . join(s)
    print(s)
if __name__ == '__main__' :
    s = "geeksforgeeks"
    x(s,'g')