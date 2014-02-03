@author: dinaaouani

#define functions that will enable me to repeat 'lines' and 'columns':

def do_twice(f):
    f()
    f()
def do_four(f):
    do_twice(f)
    do_twice(f)
    
#define horizontal lines:
    
def make_sequence():
    print '+ - - - -',
def make_row():
    do_twice(make_sequence)
    print '+'

#define vertical lines:
    
def make_bar():
    print '|        ',
def make_lines():
    do_twice(make_bar)
    print '|'   

#putting everything together to create a command that will enable me to 'print' the grid on Ipython 
def make_2boxes():
    make_row()
    do_four(make_lines)
    
def create_grid():
    do_twice(make_2boxes)
    make_row()

print create_grid()
