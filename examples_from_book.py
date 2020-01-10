Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def do_twice(f):
	f()
	f()

	
>>> def print_spam():
	print('spam')

	
>>> do_twice(print_spam)
spam
spam
>>> def do_twice(f, a):
	f(a)
	f(a)

	
>>> def print_spam(a):
	print(a)
	print(a)

	
>>> do_twice(print_spam, 'spamm')
spamm
spamm
spamm
spamm
>>> def do_four(f, a):
	do_twice(f,a)
	do_twice(f,a)

	
>>> do_four(print_spam, "SPAM")
SPAM
SPAM
SPAM
SPAM
SPAM
SPAM
SPAM
SPAM
>>> def hor_line():
	print('+','-'*4,'+','-'*4)

	
>>> hor_line
<function hor_line at 0x04092ED0>
>>> hor_line()
+ ---- + ----
>>> def hor_line():
	print('+','-'*4,'+','-'*4, end="")

	
>>> hor_line()
+ ---- + ----
>>> def hor_line():
	print('+','-'*4,'+','-'*4,'+' end="")
	
SyntaxError: invalid syntax
>>> 
>>> def hor_line():
	print('+','-'*4,'+','-'*4,'+', end="")

	
>>> hor_line()
+ ---- + ---- +
>>> def print_main_line():
	print('+','-'*4,'+','-'*4,'+', end="")

	
>>> def print_second_line():
	print('|', ''*4, '|',''*4,'|', end='')
	print('|', ''*4, '|',''*4,'|', end='')
	print('|', ''*4, '|',''*4,'|', end='')
	print('|', ''*4, '|',''*4,'|', end='')

	
>>> def square_print():
	print_main_line()
	print_second_line()
	print_main_line()
	print_second_line()
	print_main_line()

	
>>> square_print()
+ ---- + ---- +|  |  ||  |  ||  |  ||  |  |+ ---- + ---- +|  |  ||  |  ||  |  ||  |  |+ ---- + ---- +
>>> def print_main_line():
	print('+','-'*4,'+','-'*4,'+')

	
>>> def print_second_line():
	print('|', ''*4, '|',''*4,'|')
	print('|', ''*4, '|',''*4,'|')
	print('|', ''*4, '|',''*4,'|')
	print('|', ''*4, '|',''*4,'|')

	
>>> def square_print():
	print_main_line()
	print_second_line()
	print_main_line()
	print_second_line()
	print_main_line()

	
>>> square_print()
+ ---- + ---- +
|  |  |
|  |  |
|  |  |
|  |  |
+ ---- + ---- +
|  |  |
|  |  |
|  |  |
|  |  |
+ ---- + ---- +
>>> def print_second_line():
	print('|', ' '*4, '|',' '*4,'|')
	print('|', ' '*4, '|',' '*4,'|')
	print('|', ' '*4, '|',' '*4,'|')
	print('|', ' '*4, '|',' '*4,'|')

	
>>> square_print()
+ ---- + ---- +
|      |      |
|      |      |
|      |      |
|      |      |
+ ---- + ---- +
|      |      |
|      |      |
|      |      |
|      |      |
+ ---- + ---- +
>>> def print_main_line():
	print('+','-'*4,'+','-'*4,'+')

	
>>> def print_second_line():
	print('|', ' '*4, '|',' '*4,'|')
	print('|', ' '*4, '|',' '*4,'|')
	print('|', ' '*4, '|',' '*4,'|')
	print('|', ' '*4, '|',' '*4,'|')

	
>>> def square_print():
	print_main_line()
	print_second_line()
	print_main_line()

	
>>> def double_square():
	square_print()
	square_print()

	
>>> double_square
<function double_square at 0x04092FA8>
>>> double_square()
+ ---- + ---- +
|      |      |
|      |      |
|      |      |
|      |      |
+ ---- + ---- +
+ ---- + ---- +
|      |      |
|      |      |
|      |      |
|      |      |
+ ---- + ---- +
>>> def print_main_line():
	print('+','-'*4,'+','-'*4,'+')

	
>>> def print_second_line():
	print('|', ' '*4, '|',' '*4,'|')
	print('|', ' '*4, '|',' '*4,'|')
	print('|', ' '*4, '|',' '*4,'|')
	print('|', ' '*4, '|',' '*4,'|')

	
>>> def square_print():
	print_main_line()
	print_second_line()

	
>>> def double_square():
	square_print()
	square_print()

	
>>> double_square()
+ ---- + ---- +
|      |      |
|      |      |
|      |      |
|      |      |
+ ---- + ---- +
|      |      |
|      |      |
|      |      |
|      |      |
>>> def square_print():
	print_main_line()
	print_second_line()
	print_main_line()
	print_second_line()
	print_main_line()

	
>>> square_print()
+ ---- + ---- +
|      |      |
|      |      |
|      |      |
|      |      |
+ ---- + ---- +
|      |      |
|      |      |
|      |      |
|      |      |
+ ---- + ---- +
>>> def print_main_line():
	print('+','-'*4,'+','-'*4,'+','-'*4,'+')

	
>>> def print_second_line():
	print('|', ' '*4, '|',' '*4,'|', ' '*4,'|')
	print('|', ' '*4, '|',' '*4,'|', ' '*4,'|')
	print('|', ' '*4, '|',' '*4,'|', ' '*4,'|')
	print('|', ' '*4, '|',' '*4,'|', ' '*4,'|')

	
>>> def square_print():
	print_main_line()
	print_second_line()
	print_main_line()
	print_second_line()
	print_main_line()
	print_second_line()
	print_main_line()

	
>>> square_print()
+ ---- + ---- + ---- +
|      |      |      |
|      |      |      |
|      |      |      |
|      |      |      |
+ ---- + ---- + ---- +
|      |      |      |
|      |      |      |
|      |      |      |
|      |      |      |
+ ---- + ---- + ---- +
|      |      |      |
|      |      |      |
|      |      |      |
|      |      |      |
+ ---- + ---- + ---- +
>>> 
