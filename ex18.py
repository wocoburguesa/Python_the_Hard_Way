# -- coding: utf-8 --
def print_two(*args):
    arg1, arg2 = args
    print "Imprimiendo con arg[idx]-> args[0]: %r, arg[1]: %r" % (args[0], args[1])
    print "Imprimiendo las variables asignadas-> arg1: %r, arg2: %r" % (arg1, arg2)
  
#omitiendo el *args
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
  
#con solo un argumento
def print_one(arg1):
    print "arg1: %r" % arg1
  
#sin argumentos
def print_none():
    print "I got nothin'."
  
print_two("Marco", "Flores")
print_two_again("Antonio", "Nuñez")
print_one("Oz")
print_none()
