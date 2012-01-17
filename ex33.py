i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    
    i += 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
    
print "The numbers: ",

for num in numbers:
    print num,
    
print

def loop(n, inc):
    nums = []
    count = 0
    while count < n:
        nums.append(count)
        count += inc
    return nums
    
print loop(int(raw_input("Ingrese un numero para loopear: ")), int(raw_input("Ingrese un incremento: ")))
