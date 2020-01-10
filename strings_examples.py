Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def print_qq():
	print("QQ")

	
>>> print_qq
<function print_qq at 0x03BE84B0>
>>> print_qq()
QQ
>>> clear
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
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

>>> help()

Welcome to Python 3.7's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> modules

Please wait a moment while I gather a list of all available modules...

__future__          autoexpand          http                sched
__main__            base64              hyperparser         scrolledlist
_abc                bdb                 idle                search
_ast                binascii            idle_test           searchbase
_asyncio            binhex              idlelib             searchengine
_bisect             bisect              idna                secrets
_blake2             browser             imaplib             select
_bootlocale         builtins            imghdr              selectors
_bz2                bz2                 imp                 setuptools
_codecs             cProfile            importlib           shelve
_codecs_cn          calendar            inspect             shlex
_codecs_hk          calltip             io                  shutil
_codecs_iso2022     calltip_w           iomenu              signal
_codecs_jp          certifi             ipaddress           site
_codecs_kr          cgi                 itertools           six
_codecs_tw          cgitb               js_asset            smtpd
_collections        chardet             jsmin               smtplib
_collections_abc    chunk               json                sndhdr
_compat_pickle      ckeditor            keyword             socket
_compression        ckeditor_demo       lib2to3             socketserver
_contextvars        ckeditor_uploader   linecache           sqlite3
_csv                cmath               locale              sqlparse
_ctypes             cmd                 logging             squeezer
_ctypes_test        code                lzma                sre_compile
_datetime           codecontext         macosx              sre_constants
_decimal            codecs              macpath             sre_parse
_dummy_thread       codeop              mailbox             ssl
_elementtree        collections         mailcap             stackviewer
_functools          colorizer           mainmenu            stat
_hashlib            colorsys            marshal             statistics
_heapq              compileall          math                statusbar
_imp                concurrent          mimetypes           string
_io                 config              mmap                stringprep
_json               config_key          modulefinder        struct
_locale             configdialog        msilib              subprocess
_lsprof             configparser        msvcrt              suit_redactor
_lzma               contextlib          multicall           sunau
_markupbase         contextvars         multiprocessing     symbol
_md5                copy                netrc               symtable
_msi                copyreg             nntplib             sys
_multibytecodec     crypt               nt                  sysconfig
_multiprocessing    csv                 ntpath              tabnanny
_opcode             ctypes              nturl2path          tarfile
_operator           curses              numbers             telnetlib
_osx_support        dataclasses         opcode              tempfile
_overlapped         datetime            operator            test
_pickle             dateutil            optparse            testtinymce
_py_abc             dbm                 os                  textview
_pydecimal          debugger            outwin              textwrap
_pyio               debugger_r          paragraph           this
_queue              debugobj            parenmatch          threading
_random             debugobj_r          parser              time
_sha1               decimal             pathbrowser         timeit
_sha256             delegator           pathlib             tinymce
_sha3               difflib             pdb                 tkinter
_sha512             dis                 percolator          token
_signal             distutils           pickle              tokenize
_sitebuiltins       django              pickletools         tooltip
_socket             docopt              pip                 trace
_sqlite3            doctest             pipes               traceback
_sre                dummy_threading     pkg_resources       tracemalloc
_ssl                dynoption           pkgutil             tree
_stat               easy_install        platform            tty
_string             editor              plistlib            turtle
_strptime           email               poplib              turtledemo
_struct             encodings           posixpath           types
_symtable           ensurepip           pprint              typing
_testbuffer         enum                profile             undo
_testcapi           errno               pstats              unicodedata
_testconsole        faulthandler        pty                 unittest
_testimportmultiple filecmp             py_compile          urllib
_testmultiphase     fileinput           pyclbr              urllib3
_thread             filelist            pydoc               uu
_threading_local    fnmatch             pydoc_data          uuid
_tkinter            formatter           pyexpat             venv
_tracemalloc        fractions           pyparse             warnings
_warnings           ftplib              pyshell             wave
_weakref            functools           pytz                weakref
_weakrefset         gc                  query               webbrowser
_winapi             genericpath         queue               window
abc                 getopt              quopri              winreg
aifc                getpass             random              winsound
antigravity         gettext             re                  wsgiref
argparse            glob                redirector          xdrlib
array               grep                replace             xml
ast                 gzip                reprlib             xmlrpc
asynchat            hashlib             requests            xxsubtype
asyncio             heapq               rlcompleter         zipapp
asyncore            help                rpc                 zipfile
atexit              help_about          rstrip              zipimport
audioop             history             run                 zlib
autocomplete        hmac                runpy               zoomheight
autocomplete_w      html                runscript           zzdummy

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

help> math
Help on built-in module math:

NAME
    math

DESCRIPTION
    This module is always available.  It provides access to the
    mathematical functions defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.
    
    acosh(x, /)
        Return the inverse hyperbolic cosine of x.
    
    asin(x, /)
        Return the arc sine (measured in radians) of x.
    
    asinh(x, /)
        Return the inverse hyperbolic sine of x.
    
    atan(x, /)
        Return the arc tangent (measured in radians) of x.
    
    atan2(y, x, /)
        Return the arc tangent (measured in radians) of y/x.
        
        Unlike atan(y/x), the signs of both x and y are considered.
    
    atanh(x, /)
        Return the inverse hyperbolic tangent of x.
    
    ceil(x, /)
        Return the ceiling of x as an Integral.
        
        This is the smallest integer >= x.
    
    copysign(x, y, /)
        Return a float with the magnitude (absolute value) of x but the sign of y.
        
        On platforms that support signed zeros, copysign(1.0, -0.0)
        returns -1.0.
    
    cos(x, /)
        Return the cosine of x (measured in radians).
    
    cosh(x, /)
        Return the hyperbolic cosine of x.
    
    degrees(x, /)
        Convert angle x from radians to degrees.
    
    erf(x, /)
        Error function at x.
    
    erfc(x, /)
        Complementary error function at x.
    
    exp(x, /)
        Return e raised to the power of x.
    
    expm1(x, /)
        Return exp(x)-1.
        
        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    
    fabs(x, /)
        Return the absolute value of the float x.
    
    factorial(x, /)
        Find x!.
        
        Raise a ValueError if x is negative or non-integral.
    
    floor(x, /)
        Return the floor of x as an Integral.
        
        This is the largest integer <= x.
    
    fmod(x, y, /)
        Return fmod(x, y), according to platform C.
        
        x % y may differ.
    
    frexp(x, /)
        Return the mantissa and exponent of x, as pair (m, e).
        
        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
    
    fsum(seq, /)
        Return an accurate floating point sum of values in the iterable seq.
        
        Assumes IEEE-754 floating point arithmetic.
    
    gamma(x, /)
        Gamma function at x.
    
    gcd(x, y, /)
        greatest common divisor of x and y
    
    hypot(x, y, /)
        Return the Euclidean distance, sqrt(x*x + y*y).
    
    isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
        Determine whether two floating point numbers are close in value.
        
          rel_tol
            maximum difference for being considered "close", relative to the
            magnitude of the input values
          abs_tol
            maximum difference for being considered "close", regardless of the
            magnitude of the input values
        
        Return True if a is close in value to b, and False otherwise.
        
        For the values to be considered close, the difference between them
        must be smaller than at least one of the tolerances.
        
        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
        is, NaN is not close to anything, even itself.  inf and -inf are
        only close to themselves.
    
    isfinite(x, /)
        Return True if x is neither an infinity nor a NaN, and False otherwise.
    
    isinf(x, /)
        Return True if x is a positive or negative infinity, and False otherwise.
    
    isnan(x, /)
        Return True if x is a NaN (not a number), and False otherwise.
    
    ldexp(x, i, /)
        Return x * (2**i).
        
        This is essentially the inverse of frexp().
    
    lgamma(x, /)
        Natural logarithm of absolute value of Gamma function at x.
    
    log(...)
        log(x, [base=math.e])
        Return the logarithm of x to the given base.
        
        If the base not specified, returns the natural logarithm (base e) of x.
    
    log10(x, /)
        Return the base 10 logarithm of x.
    
    log1p(x, /)
        Return the natural logarithm of 1+x (base e).
        
        The result is computed in a way which is accurate for x near zero.
    
    log2(x, /)
        Return the base 2 logarithm of x.
    
    modf(x, /)
        Return the fractional and integer parts of x.
        
        Both results carry the sign of x and are floats.
    
    pow(x, y, /)
        Return x**y (x to the power of y).
    
    radians(x, /)
        Convert angle x from degrees to radians.
    
    remainder(x, y, /)
        Difference between x and the closest integer multiple of y.
        
        Return x - n*y where n*y is the closest integer multiple of y.
        In the case where x is exactly halfway between two multiples of
        y, the nearest even value of n is used. The result is always exact.
    
    sin(x, /)
        Return the sine of x (measured in radians).
    
    sinh(x, /)
        Return the hyperbolic sine of x.
    
    sqrt(x, /)
        Return the square root of x.
    
    tan(x, /)
        Return the tangent of x (measured in radians).
    
    tanh(x, /)
        Return the hyperbolic tangent of x.
    
    trunc(x, /)
        Truncates the Real x to the nearest Integral toward 0.
        
        Uses the __trunc__ magic method.

DATA
    e = 2.718281828459045
    inf = inf
    nan = nan
    pi = 3.141592653589793
    tau = 6.283185307179586

FILE
    (built-in)


help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> help(float)

>>> 
>>> help(int)

>>> help(str)

>>> help(help)
Help on _Helper in module _sitebuiltins object:

class _Helper(builtins.object)
 |  Define the builtin 'help'.
 |  
 |  This is a wrapper around pydoc.help that provides a helpful message
 |  when 'help' is typed at the Python interactive prompt.
 |  
 |  Calling help() at the Python prompt starts an interactive help session.
 |  Calling help(thing) prints help for the python object 'thing'.
 |  
 |  Methods defined here:
 |  
 |  __call__(self, *args, **kwds)
 |      Call self as a function.
 |  
 |  __repr__(self)
 |      Return repr(self).
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

>>> type(help)
<class '_sitebuiltins._Helper'>
>>> type(int)
<class 'type'>
>>> type(1)
<class 'int'>
>>> type(type)
<class 'type'>
>>> 2+2
4
>>> 4/2
2.0
>>> 4//2
2
>>> width = 20
>>> height = 5*9
>>> width*height
900
>>> 5**2
25
>>> 2**7
128
>>> 2**8
256
>>> 2**100
1267650600228229401496703205376
>>> 2*15
30
>>> 2**15
32768
>>> 2**16
65536
>>> 2*17
34
>>> 2**17
131072
>>> 2**18
262144
>>> 2**32
4294967296
>>> 0.5/100
0.005
>>> 0.5+0.5
1.0
>>> 0.1+0.1
0.2
>>> 0.1+0.3
0.4
>>> 1.1+2.2
3.3000000000000003
>>> 1.1+1.1
2.2
>>> 1.1+1.2
2.3
>>> 1.1+3.3
4.4
>>> 3.3+3.3
6.6
>>> 3.3+4.4
7.7
>>> 3.3+5.5
8.8
>>> 2.2+3.3
5.5
>>> 2.2+1.1
3.3000000000000003
>>> 1.1+_
4.4
>>> spam eggs
SyntaxError: invalid syntax
>>> apm
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    apm
NameError: name 'apm' is not defined
>>> 'spam eggs'
'spam eggs'
>>> 'doesn\'t'
"doesn't"
>>> "doesn't"
"doesn't"
>>> '"Yes," thay said'
'"Yes," thay said'
>>> "\"Yes,\" thay said"
'"Yes," thay said'
>>> '"Isn\'t" they said'
'"Isn\'t" they said'
>>> "\"Isn\'t\", they said'
SyntaxError: EOL while scanning string literal
>>> "\"Isn't\", they said"
'"Isn\'t", they said'
>>> r "\"Isn\'t\", they said'
SyntaxError: EOL while scanning string literal
>>> '''"Isn\'t", they said'''
'"Isn\'t", they said'
>>> print('C\some\name')
C\some
ame
>>> print(r'C\some\name')
C\some\name
>>> print("""\
Usage: thingy [OPTIONS]
	-h
	-H hostname
""")
Usage: thingy [OPTIONS]
	-h
	-H hostname

>>> print("""\
В лесу родилась ёлочка
В лесу она росла
Зимой и летом стройная
Зелёная была
""")
В лесу родилась ёлочка
В лесу она росла
Зимой и летом стройная
Зелёная была

>>> def print_tree():
	print("""\
В лесу родилась ёлочка
В лесу она росла
Зимой и летом стройная
Зелёная была
""")

	
>>> print_tree
<function print_tree at 0x059B7978>
>>> print_tree()
В лесу родилась ёлочка
В лесу она росла
Зимой и летом стройная
Зелёная была

>>> def right_move(a):
	print((" "*70 - len(a) + a))

	
>>> right_move("hello")
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    right_move("hello")
  File "<pyshell#80>", line 2, in right_move
    print((" "*70 - len(a) + a))
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> def right_move(a):
	print((" "*(70 - len(a)) + a))

	
>>> right_move("hello")
                                                                 hello
>>> 'Py' 'FUCK' 'thon'
'PyFUCKthon'
>>> text = ('Put some loooooong text '
            'to one loooong string.')
>>> text
'Put some loooooong text to one loooong string.'
>>> prefix = 'Py'
>>> prefix thon
SyntaxError: invalid syntax
>>> prefix*3
'PyPyPy'
>>> prefix[0]
'P'
>>> prefix[1]
'y'
>>> prefix[2]
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    prefix[2]
IndexError: string index out of range
>>> prefix[0:-1]
'P'
>>> prefix[-1]
'y'
>>> prefix[-1;0]
SyntaxError: invalid syntax
>>> prefix[-1:0]
''
>>> prefix[-1:1]
''
>>> prefix[-1:2]
'y'
>>> test_text = "python long range"
>>> test_text[i]
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    test_text[i]
NameError: name 'i' is not defined
>>> test_text[i:]
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    test_text[i:]
NameError: name 'i' is not defined
>>> test_text[:1]
'p'
>>> test_text[1:]
'ython long range'
>>> test_text[:2]
'py'
>>> test_text[1:3]
'yt'
>>> test_text[0:2]
'py'
>>> len(test_text)
17
>>> test_text[17:]
''
>>> test_text[0]
'p'
>>> test_text[0] = '1'
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    test_text[0] = '1'
TypeError: 'str' object does not support item assignment
>>> list[1,2,3,4,5,6,7,8,9,]
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    list[1,2,3,4,5,6,7,8,9,]
TypeError: 'type' object is not subscriptable
>>> list[1,2,3,4,5,6,7,8,9]
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    list[1,2,3,4,5,6,7,8,9]
TypeError: 'type' object is not subscriptable
>>> list = [1,2,3,4,5,6,7,8,9,]
>>> list
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list[0]
1
>>> list[1:]
[2, 3, 4, 5, 6, 7, 8, 9]
>>> len(list)
9
>>> list[0] = 0
>>> list
[0, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list = [0,1,2,3,4,5,6,7,8,9,]
>>> list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> len(list)
10
>>> type(list)
<class 'list'>
>>> type('list')
<class 'str'>
>>> type
<class 'type'>
>>> list*3
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list/10
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    list/10
TypeError: unsupported operand type(s) for /: 'list' and 'int'
>>> list/3
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    list/3
TypeError: unsupported operand type(s) for /: 'list' and 'int'
>>> list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list-list
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    list-list
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> list = list + list
>>> list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list.append[list[0]]
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    list.append[list[0]]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> list.append[111]
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    list.append[111]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> list.append(list[0])
>>> list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
>>> def test_test(i, j):
	for j > 0:list.append(list[0])
	
SyntaxError: invalid syntax
>>> def test_test(i, j):
	while j > 0:
		j--
		list.append(list[j])
		list = list[0:j]
		
SyntaxError: invalid syntax
>>> def test_test(i, j):
	while j > 0:
		--j
		list.append(list[j])
		list = list[0:j]

		
>>> test_test (2, 8)
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    test_test (2, 8)
  File "<pyshell#145>", line 4, in test_test
    list.append(list[j])
UnboundLocalError: local variable 'list' referenced before assignment
>>> list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
>>> list = [0,1,2,3,4,5,6,7,8,9]
>>> list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list*3
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list[0] = 111
>>> list
[111, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list[0] = 0
>>> list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list + list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> print(list)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a, b = 0,1
>>> while a< 10:
	print(a)
	a, b = b, a+b

	
0
1
1
2
3
5
8
>>> while a < 100:
	print(a)
	a, b = b, a+b

	
13
21
34
55
89
>>> a, b = 0,1
>>> while a < 1000:
	print(a)
	a, b = b, a+b

	
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
>>> i = 'FUCK'
>>> print('i is absolutely', i)
i is absolutely FUCK
>>> print(list, end=',')
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
>>> x = 1
>>> y = 2
>>> print(x, y, end = ',')
1 2,
>>> print(x,y,x,y,x,y)
1 2 1 2 1 2
>>> print(xy)
Traceback (most recent call last):
  File "<pyshell#178>", line 1, in <module>
    print(xy)
NameError: name 'xy' is not defined
>>> print(x y)
SyntaxError: invalid syntax
>>> print(x, y, y, x, end=';')
1 2 2 1;
>>> list = "python is a capital of great britain"
>>> list.capitalize()
'Python is a capital of great britain'
>>> list.casefold()
'python is a capital of great britain'
>>> list2 = "PYTHON"
>>> list2.casefold()
'python'
>>> list.center
<built-in method center of str object at 0x0592DF60>
>>> list.center()
Traceback (most recent call last):
  File "<pyshell#187>", line 1, in <module>
    list.center()
TypeError: center() takes at least 1 argument (0 given)
>>> list.center(100)
'                                python is a capital of great britain                                '
>>> list.count(1)
Traceback (most recent call last):
  File "<pyshell#189>", line 1, in <module>
    list.count(1)
TypeError: must be str, not int
>>> list.count('hello')
0
>>> list.count('0')
0
>>> list
'python is a capital of great britain'
>>> list.count('g')
1
>>> list.count('p')
2
>>> list.count('p', 5, 15)
1
>>> List
Traceback (most recent call last):
  File "<pyshell#196>", line 1, in <module>
    List
NameError: name 'List' is not defined
>>> list
'python is a capital of great britain'
>>> type(list)
<class 'str'>
>>> type(List)
Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    type(List)
NameError: name 'List' is not defined
>>> 
>>> type([])
<class 'list'>
>>> 'list'
'list'
>>> list.encode()
b'python is a capital of great britain'
>>> list
'python is a capital of great britain'
>>> list.endswith('in')
True
>>> list.endswith('al')
False
>>> list.endswith('ain')
True
>>> list.endswith(('ain', 'lin', 'man'))
True
>>> list.endswith(('ani', 'lin', 'man'))
False
>>> list.endswith(('ain', 'lin', 'man'))
True
>>> list.expandtabs()
'python is a capital of great britain'
>>> list
'python is a capital of great britain'
>>> list = '			python is a capital of great britain'
>>> list.expandtabs()
'                        python is a capital of great britain'
>>> list
'\t\t\tpython is a capital of great britain'
>>> list = '			python is a capital of great britain'
>>> list
'\t\t\tpython is a capital of great britain'
>>> list.expandtabs(tabsize=1)
'   python is a capital of great britain'
>>> list.expandtabs(tabsize=0)
'python is a capital of great britain'
>>> list.expandtabs(tabsize=2)
'      python is a capital of great britain'
>>> list.expandtabs(tabsize=3)
'         python is a capital of great britain'
>>> list
'\t\t\tpython is a capital of great britain'
>>> list = 'python is a capital of great britain'
>>> list
'python is a capital of great britain'
>>> list.find(py)
Traceback (most recent call last):
  File "<pyshell#225>", line 1, in <module>
    list.find(py)
NameError: name 'py' is not defined
>>> list.find('py')
0
>>> list.find('yp')
-1
>>> list.find('cap')
12
>>> list.format()
'python is a capital of great britain'
>>> list.format(1+2)
'python is a capital of great britain'
>>> list.format(1+2)
'python is a capital of great britain'
>>> list.index('in')
34
>>> list.index('iny')
Traceback (most recent call last):
  File "<pyshell#233>", line 1, in <module>
    list.index('iny')
ValueError: substring not found
>>> list.index('p')
0
>>> list.index('i')
7
>>> list.isal()
Traceback (most recent call last):
  File "<pyshell#236>", line 1, in <module>
    list.isal()
AttributeError: 'str' object has no attribute 'isal'
>>> list.isalnum()
False
>>> list.isalnum()
False
>>> list2 = "a b c d e f g"
>>> list2.isalnum()
False
>>> list2 = "a b c d e f g 1"
>>> list2.isalnum()
False
>>> >>> list2 = "1 2 3 a b c"
SyntaxError: invalid syntax
>>> list2 = "1 2 3 a b c"
>>> list2.isalnum()
False
>>> list2 = "123abc"
>>> list2.isalnum()
True
>>> list2 = "1 23abc"
>>> list2.isalnum()
False
>>> list2 = "123abc"
>>> list2.isalnum()
True
>>> list2 = 123
>>> list2
123
>>> list2.isdigit()
Traceback (most recent call last):
  File "<pyshell#254>", line 1, in <module>
    list2.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
>>> list2 = "123"
>>> list2.isdigit()
True
>>> list2.isnumeric()
True
>>> list2.islower()
False
>>> list3 = "dfasdfsd"
>>> list3.islower()
True
>>> list3.isprintable
<built-in method isprintable of str object at 0x058994D0>
>>> list3.isprintable()
True
>>> list3.isspace()
False
>>> 
KeyboardInterrupt
>>> list1.isspace()
Traceback (most recent call last):
  File "<pyshell#264>", line 1, in <module>
    list1.isspace()
NameError: name 'list1' is not defined
>>> list.isspace()
False
>>> list
'python is a capital of great britain'
>>> list2.isspace()
False
>>> list2
'123'
>>> list2 = '1 2 3'
>>> list2.isspace()
False
>>> list2.istitle()
False
>>> list.istitle()
False
>>> list
'python is a capital of great britain'
>>> list4 = "Python is a king"
>>> list4.istitle()
False
>>> list4
'Python is a king'
>>> list4 = "I'M THE LIZARD KING"
>>> list4.isupper()
True
>>> list4.join('Ivan FUCKoff')
"II'M THE LIZARD KINGvI'M THE LIZARD KINGaI'M THE LIZARD KINGnI'M THE LIZARD KING I'M THE LIZARD KINGFI'M THE LIZARD KINGUI'M THE LIZARD KINGCI'M THE LIZARD KINGKI'M THE LIZARD KINGoI'M THE LIZARD KINGfI'M THE LIZARD KINGf"
>>> list4.join(1)
Traceback (most recent call last):
  File "<pyshell#280>", line 1, in <module>
    list4.join(1)
TypeError: can only join an iterable
>>> list4.join(2)
Traceback (most recent call last):
  File "<pyshell#281>", line 1, in <module>
    list4.join(2)
TypeError: can only join an iterable
>>> list4.join('A')
'A'
>>> 'A'.join(list4)
"IA'AMA ATAHAEA ALAIAZAAARADA AKAIANAG"
>>> '---'.join(list4)
"I---'---M--- ---T---H---E--- ---L---I---Z---A---R---D--- ---K---I---N---G"
>>> '\n'.join(list4)
"I\n'\nM\n \nT\nH\nE\n \nL\nI\nZ\nA\nR\nD\n \nK\nI\nN\nG"
>>> '-'.join(list4)
"I-'-M- -T-H-E- -L-I-Z-A-R-D- -K-I-N-G"
>>> list4.ljust()
Traceback (most recent call last):
  File "<pyshell#287>", line 1, in <module>
    list4.ljust()
TypeError: ljust() takes at least 1 argument (0 given)
>>> list4.ljust(1)
"I'M THE LIZARD KING"
>>> 
>>> list4.ljust(10)
"I'M THE LIZARD KING"
>>> list4.ljust(100)
"I'M THE LIZARD KING                                                                                 "
>>> list4.ljust(70)
"I'M THE LIZARD KING                                                   "
>>> list4.maketrans(1)
Traceback (most recent call last):
  File "<pyshell#293>", line 1, in <module>
    list4.maketrans(1)
TypeError: if you give only one argument to maketrans it must be a dict
>>> list4.maketrans(1, 1, 1)
Traceback (most recent call last):
  File "<pyshell#294>", line 1, in <module>
    list4.maketrans(1, 1, 1)
TypeError: maketrans() argument 2 must be str, not int
>>> in_tab = 'abcdefghij'
>>> out_tab = '0123456789'
>>> tran_tab = maketrans(in_tab, out_tab)
Traceback (most recent call last):
  File "<pyshell#297>", line 1, in <module>
    tran_tab = maketrans(in_tab, out_tab)
NameError: name 'maketrans' is not defined
>>> from string import maketrans
Traceback (most recent call last):
  File "<pyshell#298>", line 1, in <module>
    from string import maketrans
ImportError: cannot import name 'maketrans' from 'string' (C:\Users\Admin\AppData\Local\Programs\Python\Python37-32\lib\string.py)
>>> str.maketrans(in_tab, out_tab)
{97: 48, 98: 49, 99: 50, 100: 51, 101: 52, 102: 53, 103: 54, 104: 55, 105: 56, 106: 57}
>>> list4.maketrans(in_tab, out_tab)
{97: 48, 98: 49, 99: 50, 100: 51, 101: 52, 102: 53, 103: 54, 104: 55, 105: 56, 106: 57}
>>> list4
"I'M THE LIZARD KING"
>>> list4.partition("L")
("I'M THE ", 'L', 'IZARD KING')
>>> list4.partition(" ")
("I'M", ' ', 'THE LIZARD KING')
>>> list4.replace("KING", "QUEEN")
"I'M THE LIZARD QUEEN"
>>> list4
"I'M THE LIZARD KING"
>>> list4.rfind()
Traceback (most recent call last):
  File "<pyshell#306>", line 1, in <module>
    list4.rfind()
TypeError: rfind() takes at least 1 argument (0 given)
>>> list4.rfind("L")
8
>>> list4.rfind("E")
6
>>> list4.rfind("I")
16
>>> list4.rindex('I')
16
>>> list4.rindex('Y')
Traceback (most recent call last):
  File "<pyshell#311>", line 1, in <module>
    list4.rindex('Y')
ValueError: substring not found
>>> list4
"I'M THE LIZARD KING"
>>> list4.rjust(90)
"                                                                       I'M THE LIZARD KING"
>>> list4.rjust(70)
"                                                   I'M THE LIZARD KING"
>>> list4.ljust(90)
"I'M THE LIZARD KING                                                                       "
>>> list4.partition(" ")
("I'M", ' ', 'THE LIZARD KING')
>>> list4.partition("Z")
("I'M THE LI", 'Z', 'ARD KING')
>>> list4.partition("O")
("I'M THE LIZARD KING", '', '')
>>> list4.rpartition("O")
('', '', "I'M THE LIZARD KING")
>>> list4.split(" ")
["I'M", 'THE', 'LIZARD', 'KING']
>>> list4.rsplit(" ")
["I'M", 'THE', 'LIZARD', 'KING']
>>> list4.split("O")
["I'M THE LIZARD KING"]
>>> list4.rsplit("O")
["I'M THE LIZARD KING"]
>>> list4.rsplit("I")
['', "'M THE L", 'ZARD K', 'NG']
>>> list4.split("I")
['', "'M THE L", 'ZARD K', 'NG']
>>> list4.rstrip()
"I'M THE LIZARD KING"
>>> list4.rstrip("LIBEW")
"I'M THE LIZARD KING"
>>> list4
"I'M THE LIZARD KING"
>>> list4.rstrip('KING')
"I'M THE LIZARD "
>>> list4.rstrip('LIZ')
"I'M THE LIZARD KING"
>>> list4.rstrip('THE')
"I'M THE LIZARD KING"
>>> list4.rstrip('LIZARD KING')
"I'M THE"
>>> list4.strip('THE')
"I'M THE LIZARD KING"
>>> list4.strip('ITHE')
"'M THE LIZARD KING"
>>> list4.splitlines('\n')
Traceback (most recent call last):
  File "<pyshell#335>", line 1, in <module>
    list4.splitlines('\n')
TypeError: an integer is required (got type str)
>>> list4.splitlines()
["I'M THE LIZARD KING"]
>>> list4.splitlines(0)
["I'M THE LIZARD KING"]
>>> list4.splitlines(1)
["I'M THE LIZARD KING"]
>>> list4.startswith()
Traceback (most recent call last):
  File "<pyshell#339>", line 1, in <module>
    list4.startswith()
TypeError: startswith() takes at least 1 argument (0 given)
>>> list4.startswith("I")
True
>>> list4.startswith(" ")
False
>>> list4
"I'M THE LIZARD KING"
>>> list4.strip()
"I'M THE LIZARD KING"
>>> list4.strip(' ')
"I'M THE LIZARD KING"
>>> list4.strip("")
"I'M THE LIZARD KING"
>>> list4.strip(" ")
"I'M THE LIZARD KING"
>>> list4.strip("'")
"I'M THE LIZARD KING"
>>> list4
"I'M THE LIZARD KING"
>>> list4 = "!!!!!!!.......I'M THE LIZARD KING!!!!!!!.......#####"
>>> list4.strip("!.#")
"I'M THE LIZARD KING"
>>> list4.strip(".#!")
"I'M THE LIZARD KING"
>>> list4.strip("#./!")
"I'M THE LIZARD KING"
>>> list4.strip("#!")
".......I'M THE LIZARD KING!!!!!!!......."
>>> list4 = "I'M THE LIZARD KING"
>>> list4
"I'M THE LIZARD KING"
>>> list4.swapcase()
"i'm the lizard king"
>>> list4.title()
"I'M The Lizard King"
>>> list4
"I'M THE LIZARD KING"
>>> list5 = '777'
>>> list5.zfill()
Traceback (most recent call last):
  File "<pyshell#360>", line 1, in <module>
    list5.zfill()
TypeError: zfill() takes exactly one argument (0 given)
>>> list5.zfill(8)
'00000777'
>>> list5.zfill(-1)
'777'
>>> list5.zfill(-5)
'777'
>>> list5.zfill(-10)
'777'
>>> 
