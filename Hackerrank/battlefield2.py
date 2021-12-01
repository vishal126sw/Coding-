from random import randint
if __name__ == '__main__':
# Both the persons will be agreed upon the
# public keys G and P
# A prime number P is taken
    P = 17
    # A primitve root for P, G is taken
    G = 5
    print('The Value of P is :%d'%(P))
    print('The Value of G is :%d'%(G))
    # Alice will choose the private key a
    a = 4
    print('The Private Key a for Alice is :%d'%(a))
    # gets the generated key
    x = int(pow(G,a,P))
    # Bob will choose the private key b
    b = 3
    print('The Private Key b for Bob is :%d'%(b))
    # gets the generated key
    y = int(pow(G,b,P))
    # Secret key for Alice
    ka = int(pow(y,a,P))
    # Secret key for Bob
    kb = int(pow(x,b,P))
    print('Secret key for the Alice is : %d'%(ka))
    print('Secret Key for the Bob is : %d'%(kb))
"""output:
The Value of P is :17
The Value of G is :5
The Private Key a for Alice is :4
The Private Key b for Bob is :3
Secret key for the Alice is : 4
Secret Key for the Bob is: 4"""