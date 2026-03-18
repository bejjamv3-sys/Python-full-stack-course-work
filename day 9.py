Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s={}
type(s)
<class 'dict'>
s=set()
s={5678,65678,34,67,}
s
{65678, 34, 67, 5678}
s.add("string")
s
{34, 67, 'string', 65678, 5678}
s.add(2+3j)
s
{34, 67, (2+3j), 'string', 65678, 5678}
s.add(false)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s.add(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
s.add(False)
s
{False, 34, 67, (2+3j), 'string', 65678, 5678}
s.add({1,2,3})
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s.add({1,2,3})
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
s
{False, 34, 67, (2+3j), 'string', 65678, 5678}
s.add(1)
s
{False, 1, 34, 67, (2+3j), 'string', 65678, 5678}
s.update({2,3,4})
s
{False, 1, 34, 67, 2, 3, 4, (2+3j), 'string', 65678, 5678}
s.pop()
False
s.pop()
1
>>> s.pop()
34
>>> s.pop()
67
>>> s
{2, 3, 4, (2+3j), 'string', 65678, 5678}
>>> s.remove(3)
>>> s
{2, 4, (2+3j), 'string', 65678, 5678}
>>> s.discard(3)
>>> s
{2, 4, (2+3j), 'string', 65678, 5678}
>>> for i in s:
...     print(i)
... 
...     
2
4
(2+3j)
string
65678
5678
>>> 
>>> a={9,7,5,3,1,}
>>> b={2,3,4,5}
>>> a & b
{3, 5}
>>> a | b
{1, 2, 3, 4, 5, 7, 9}
>>> a-b
{1, 9, 7}
>>> #{9},{7},{5}
>>> {9}<a
True
>>> a.isdisjoint(b)
False
>>> {0} . isdisjoint(a)
True
>>> a. union(b)
{1, 2, 3, 4, 5, 7, 9}
>>> a.intersection(b)
{3, 5}
>>> a
{1, 3, 5, 7, 9}
>>> len(a)
5
>>> max(a)
9
>>> min(a)
1
>>> sorted(a)
[1, 3, 5, 7, 9]
