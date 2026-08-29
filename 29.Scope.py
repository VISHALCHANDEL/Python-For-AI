"""
doc String
"""

glob = 'hi iam globally available'


def f1():
    local = "Hii i am locally available"
    print(local)
    print(glob)

f1()