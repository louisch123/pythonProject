#print('Hello TripleTen')#
#Test - Function compares two values#
def in_autotests_we_trust(a, b):
    if a == b:
        print('Test passed')
    else:
        print('Test failed')

in_autotests_we_trust(10, '10')# This would not pass because an int =! to a str#

in_autotests_we_trust(0, False)#This would pass because a Boolean values True ==1, and False == 0 or 0.0#