def pal(word):
    d = word[::-1]
    if word == d :
        print "it is palindrome"
    else:
        print "it is not palindrome"
a = raw_input("enter the number or string \t")
pal(a)
