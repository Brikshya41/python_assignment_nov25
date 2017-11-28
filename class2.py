Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def greeting():
	print("------------------")
	print("   Hello World    ")
	print("------------------")

	
>>> greeting()
------------------
   Hello World    
------------------
>>> def sum_two_numbers(num1,num2):
	total = num1+num2
	print("{}+{}={}".format(num1,num2,total))

	
>>> sum_two_numbers(3,4)
3+4=7
>>> big=max('Hello world')
>>> print(big)
w
>>> def f(x):
	y=2*x+3
	print("2x+3={}".format(y))

	
>>> f(3)
2x+3=9
>>> def num_square(num):
	return num*num

>>> my_num=3
>>> print(num_square(2))
4
>>> print(num_aquare(my_num))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(num_aquare(my_num))
NameError: name 'num_aquare' is not defined
>>> print(num_sqyare(2))
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(num_sqyare(2))
NameError: name 'num_sqyare' is not defined
>>> f(3)
2x+3=9
>>> def num_square(num):
	return num*num

>>> my_num=3
>>> print(num_square(2))
4
SyntaxError: multiple statements found while compiling a single statement
>>> def num_square(num):
	return num*num

>>> my_num=3
>>> print(num_square(2))
4
>>> print(num_square(my_num))
9
>>> 
========== RESTART: C:/Users/User/Desktop/Project/sem3/function.py ==========
2x+3=9
>>> def greeting(style_char='-'):
	print(style_char*29)
	print("	    Hello World      ")
	print(style_char*29)

	
>>> print("Default style")
Default style
>>> greeting()
-----------------------------
	    Hello World      
-----------------------------
>>> print("\nStyle character*")

Style character*
>>> greeting('*')
*****************************
	    Hello World      
*****************************
>>> print("\nStyle character=")

Style character=
>>> greeting(style_char='=')
=============================
	    Hello World      
=============================
>>> type(1)
<class 'int'>
>>> type(1.0)
<class 'float'>
>>> type("1.0")
<class 'str'>
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> a=5
>>> b=2
>>> print(a+b,a-b)
7 3
>>> print(a+b, a-b, sep=':')
7:3
>>> print(a+b, a-b, sep=',')
7,3
>>> print(1,2,3, end="", sep=":")
1:2:3
>>> x=2
>>> y="Hello"
>>> x+y
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    x+y
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> str(x)+y
'2Hello'
>>> appx_pi=22/7
>>> print("{0:.2f}".format(appx_pi))
3.14
>>> print("{0:<10.3f}".format(appx_pi))
3.143     
>>> print)"{0:<10.3f} and 5.12".fprmat(appx_pi))
SyntaxError: invalid syntax
>>> print("{0:<10.3f) and 5.12".format(appx_pi))
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    print("{0:<10.3f) and 5.12".format(appx_pi))
ValueError: unmatched '{' in format spec
>>> print("{0:>10.3f} and 5.12".format(appx_pi))
     3.143 and 5.12
>>> x=range(1,10)
>>> x
range(1, 10)
>>> for each in x:
	print each
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(each)?
>>> foe each in x:
	
SyntaxError: invalid syntax
>>> for each in x:
	print(each)

	
1
2
3
4
5
6
7
8
9
>>> for each in range(1,10,2):
	print(each)

	
1
3
5
7
9
>>> import OS
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    import OS
ModuleNotFoundError: No module named 'OS'
>>> import os
>>> os.system("CLS")
0
>>> 
