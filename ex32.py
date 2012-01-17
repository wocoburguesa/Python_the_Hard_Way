the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# for
for number in the_count:
    print "This is count %d" % number
    
#same
for fruit in fruits:
    print "A fruit of type %s" % fruit
    
#mixed list
#se usa %r ya que no se sabe que tipo de dato es
for i in change:
    print "I got %r" % i
    
#construir listas
elements = []

#range
for i in range(0, 600):
    print "Adding %d to the list." % i
    #append
    elements.append(i)
    
#imprimiendo
for i in elements:
    print "Element was: %d" % i
