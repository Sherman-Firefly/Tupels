def palindrome(r):
    a=len(r)-1
    b=0
    while b<a:
        if r[b]!=a:
            return False
        b+=1
        a-=1
    return True
r=(1,2,3,3,2,1)

if(palindrome(r)):
    print("Tuple is a palindrome")
else:
    print("Tuple is not a palindrome")