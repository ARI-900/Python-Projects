# try:
#     a,b = [int(a) for a in input("Enter two number: ").split()]
#     assert not(b == 5), ('Five Division Error ...')
#     c = a//b
#     print('Division: ',c)
#
# except ValueError as msg:
#     print('Valuue Error ...')
# except AssertionError as msg:
#     print(msg)
# except ZeroDivisionError as msg:
#     print("Zero Division Error")
#
# class FiveDivisionError(Exception):
#     pass
# try:
#     a,b = [int(n) for n in input("Enter two number: ").split()]
#     if b == 5:
#         raise FiveDivisionError ('Five Division Error ...')
#     c = a//b
#     print("Division: ",c)
#
# except ValueError as msg:
#     print("Value Error....")
# except FiveDivisionError as msg:
#     print(msg)
# except ZeroDivisionError as msg:
#     print(msg)

