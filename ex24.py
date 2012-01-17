print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of loce
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "----------------"
print poem
print "----------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
    
    
start_point = 10000
beans, jars, crates = secret_formula(start_point)

#hola = secret_formula(start_point)
#hola[0] = 999
#chao = (1, 3)
#print "PARENTESIS: %d %d %d %d" % (hola[0], hola[1], hola[2], chao[0])
# UN RETURN DE VARIOS ELEMENTOS DEVUELVE TUPLA, NO LISTA

print "WIth a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
