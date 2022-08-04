def my_func2(a):
    d = pow(a,3)
    return d;





def my_func1(a):
    c =  pow(a,2)
    return c;
 


def my_func(a):
    if a %2==0 :
        return my_func1(a)
    else :
        return my_func2(a)

    
a = int(input())
x=my_func(a)
print(x)