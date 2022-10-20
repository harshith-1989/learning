# def foo(n):
#     if (n<3): yield 1
#     else: return
#     yield 2
#
#
# n=2
# f=foo(n)
# for i in range(n): print(f.__next__())
#
#
# n=5
# f=foo(n)
# for i in range(n): print(f.__next__())


#import builtins; print(builtins.__dict__.keys())


# t= tuple(1,2,3)
# print(type(t))

# class Mytype(type): pass
# class subtype(Mytype): pass
# class myobj(object):
#     __metaclass__ = Mytype
#
# print(Mytype.__class__)
# print(subtype.__class__)
# print(myobj.__class__)


# a = {1,2,3}
# b = {3,4,5}
#
# print(a^b)


# import sys; print(sys.builtin_module_names)

# def multipliers():
#     return [lambda x: i*x for i in range(4)]
#
# print([m(2) for m in multipliers()])

# print('{0:$>2d} * {1:$>2d} = {2:$>2d}'.format(5,10,5*10))

# class A: pass
# class B(A): pass
# class C(object): pass
# class D(C): pass
#
# a = A()
# b = B()
# c= C()
# d = D()
#
# print(isinstance(a, type(b)))
# print(issubclass(C,C))
# print(isinstance(d,D))
# print(issubclass(C,(D,A,B,C)))

# d1 = dict()
# d1 = {1,4}
# print(type(d1))
# import warnings
#
#
# def deprecated(func):
#     def nfunc(*args, **kwargs):
#         warnings.warn('call deprecated{}'.format(func.__name__), category=DeprecationWarning)
#         return func(*args, **kwargs)
#     return nfunc
#
# @deprecated
# def prod(x,y):
#     'ret prod'
#     return x*y
#
# print(prod(12,12))
# print(prod.__name__)
# print(prod.__doc__)


# a=(5)
# print(type(a))


# class B:
#     pass
#
# class A:
#     __metatype__=B


# class MyErr(Exception):
#     def __init__(self, value):
#         self.value = value
#     def __str__(self):
#         return repr(self.value)
#
# try:
#     print("hello world!")
#     raise MyErr("Oops")
# except MyErr as e:
#     print("errr: ",e)

# def f1(a,b):
#     f1.s = 'sv'
#     return a+b
#
# try:
#     print(f1.s)
# except Exception as e:
#     print(str(e))
#
# f1(3,4)
#
# try:
#     print(f1.s)
# except Exception as e:
#     print(str(e))


# import logging
# logging.warning("warn")
# logging.info("i")
# logging.error("e")
# logging.debug("d")

# class c1:
#     a=1
#
#     def f():
#         a=2
#         c1.a+=1
#         print(c1.a)
#         print(a)
#
# c1.f()
# c1.f()

# def f(**kw):
#     x =1,2,3
#     a,b,c = 1,2,3
#     z=0
#     y=z
#     d,e = 1,2,3
#
# f()