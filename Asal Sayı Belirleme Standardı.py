import random
import math
import gmpy2
from gmpy2 import mpz,mpq,mpfr,mpc
import traceback

bit = int(input('kaç bitlik şifreleme yapmak istiyorsunuz:'))
n = bit/2
n = int(n)
m = pow(2,n-3)
s = int((math.log10(2) * n) - 1)


list = ["c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1",
         "c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1","c1",
         "c2","c2","c2","c2","c2","c2","c2","c2","c2","c2","c2","c2","c2","c2","c2","c2","c2","c2","c2","c2","c2","c2","c2","c2","c2","c2","c2","c2","c2","c2","c2","c2",
         "c3","c3","c3","c3","c3","c3","c3","c3","c3","c3","c3","c3","c3","c3","c3","c3",
         "c4","c4","c4","c4","c4","c4","c4","c4",
         "c5","c5","c5","c5","c5","c5","c5","c5","c5","c5","c5","c5","c5","c5","c5","c5",
         "c6","c6","c6","c6","c6","c6","c6","c6",
         "c7","c7","c7","c7",
         "c8","c8","c8","c8",
         "c9","c9",
         "c10"]
def RSA():
    random_range = random.choice(list)
    #print(random_range)
    if random_range == "c1":
        y_min = 23.66
        y_max = 26.66
        y = random.uniform(y_min,y_max)
        gmpy2.get_context().precision = n
        y = (mpfr(y))
        x_min = 33.47
        x_max = 53.33
        x = random.uniform(x_min,x_max)
        gmpy2.get_context().precision = n
        x = (mpfr(x))
        r_min = x_min/y_min
        r_max = x_max/y_max
        r = random.uniform(r_min,r_max)
        gmpy2.get_context().precision = n
        r = (mpfr(r))
    elif random_range == "c2":
        y_min = 23.66
        y_max = 24.37
        y = random.uniform(y_min,y_max)
        gmpy2.get_context().precision = n
        y = (mpfr(y))
        x_min = 33.47
        x_max = 68.95
        x = random.uniform(x_min,x_max)
        gmpy2.get_context().precision = n
        x = (mpfr(x))
        r_min = x_min/y_min
        r_max = x_max/y_max
        r = random.uniform(r_min,r_max)
        gmpy2.get_context().precision = n
        r = (mpfr(r))
    elif random_range == "c3":
        y_min = 19.35
        y_max = 23.66
        y = random.uniform(y_min,y_max)
        gmpy2.get_context().precision = n
        y = (mpfr(y))
        x_min = 33.47
        x_max = 77.41
        x = random.uniform(x_min,x_max)
        gmpy2.get_context().precision = n
        x = (mpfr(x))
        r_min = x_min/y_min
        r_max = x_max/y_max
        r = random.uniform(r_min,r_max)
        gmpy2.get_context().precision = n
        r = (mpfr(r))
    elif random_range == "c4":
        y_min = 15.02
        y_max = 23.66
        y = random.uniform(y_min,y_max)
        gmpy2.get_context().precision = n
        y = (mpfr(y))
        x_min = 33.47
        x_max = 84.97
        x = random.uniform(x_min,x_max)
        gmpy2.get_context().precision = n
        x = (mpfr(x))
        r_min = x_min/y_min
        r_max = x_max/y_max
        r = random.uniform(r_min,r_max)
        gmpy2.get_context().precision = n
        r = (mpfr(r))
    elif random_range == "c5":
        y_min = 24.37
        y_max = 26.66
        y = random.uniform(y_min,y_max)
        gmpy2.get_context().precision = n
        y = (mpfr(y))
        x_min = 53.33
        x_max = 68.95
        x = random.uniform(x_min,x_max)
        gmpy2.get_context().precision = n
        x = (mpfr(x))
        r_min = x_min/y_min
        r_max = x_max/y_max
        r = random.uniform(r_min,r_max)
        gmpy2.get_context().precision = n
        r = (mpfr(r))
    elif random_range == "c6":
        y_min = 19.35
        y_max = 26.66
        y = random.uniform(y_min,y_max)
        gmpy2.get_context().precision = n
        y = (mpfr(y))
        x_min = 53.33
        x_max = 77.41
        x = random.uniform(x_min,x_max)
        gmpy2.get_context().precision = n
        x = (mpfr(x))
        r_min = x_min/y_min
        r_max = x_max/y_max
        r = random.uniform(r_min,r_max)
        gmpy2.get_context().precision = n
        r = (mpfr(r))
    elif random_range == "c7":
        y_min = 15.02
        y_max = 26.66
        y = random.uniform(y_min,y_max)
        gmpy2.get_context().precision = n
        y = (mpfr(y))
        x_min = 53.33
        x_max = 84.97
        x = random.uniform(x_min,x_max)
        gmpy2.get_context().precision = n
        x = (mpfr(x))
        r_min = x_min/y_min
        r_max = x_max/y_max
        r = random.uniform(r_min,r_max)
        gmpy2.get_context().precision = n
        r = (mpfr(r))
    elif random_range == "c8":
        y_min = 19.35
        y_max = 24.37
        y = random.uniform(y_min,y_max)
        gmpy2.get_context().precision = n
        y = (mpfr(y))
        x_min = 68.95
        x_max = 77.41
        x = random.uniform(x_min,x_max)
        gmpy2.get_context().precision = n
        x = (mpfr(x))
        r_min = x_min/y_min
        r_max = x_max/y_max
        r = random.uniform(r_min,r_max)
        gmpy2.get_context().precision = n
        r = (mpfr(r))
    elif random_range == "c9":
        y_min = 15.02
        y_max = 24.37
        y = random.uniform(y_min,y_max)
        gmpy2.get_context().precision = n
        y = (mpfr(y))
        x_min = 68.95
        x_max = 84.97
        x = random.uniform(x_min,x_max)
        gmpy2.get_context().precision = n
        x = (mpfr(x))
        r_min = x_min/y_min
        r_max = x_max/y_max
        r = random.uniform(r_min,r_max)
        gmpy2.get_context().precision = n
        r = (mpfr(r))
    else:
        y_min = 15.02
        y_max = 19.35
        y = random.uniform(y_min,y_max)
        gmpy2.get_context().precision = n
        y = (mpfr(y))
        x_min = 77.41
        x_max = 84.97
        x = random.uniform(x_min,x_max)
        gmpy2.get_context().precision = n
        x = (mpfr(x))
        r_min = x_min/y_min
        r_max = x_max/y_max
        r = random.uniform(r_min,r_max)
        gmpy2.get_context().precision = n
        r = (mpfr(r))
    if ((x+y) > 100):
        RSA()
    z = 100 - x - y
    gmpy2.get_context().precision = n
    z = (mpfr(z))
    a = (pow(x,2) - 200 * x + 10000 - 100 * z) / (10000)
    gmpy2.get_context().precision = n
    a = (mpfr(a))
    b = (((50 * m * (2 * x + z - 100)) - (pow(x,2) * m)) / 5000)
    gmpy2.get_context().precision = n
    b = (mpfr(b))
    c = (pow(x,2) * pow(m,2) / 10000)
    gmpy2.get_context().precision = n
    c = (mpfr(c))
    b_2 = pow(b,2)
    gmpy2.get_context().precision = n
    a_c_4 = mpfr(4 * a * c)
    b_2_a_c_4 = int(b_2 - a_c_4)
    delta = gmpy2.isqrt(b_2_a_c_4)
    #print(delta)
    q = ((-b + delta) / ( 2 * a))
    q = int(q)
    #print ("q Sayısı:",int(q))
    if (q < 0):
        RSA()
    p = pow(((z * ((q - m) / 100) + m) + (((q - m) / 100) * y)) / gmpy2.isqrt(q),2)
    #print("p Sayısı:",int(p))
    p = int(p)
    alfa_p = 10 * math.log(p, math.e)
    alfa_p = int(alfa_p)
    #print("alfa_p:",alfa_p)
    beta_p = p - alfa_p
    beta_p = int(beta_p)
    #print("beta_p:",beta_p)
    while p > beta_p:
        if p % 2 == 0:
            p -= 1
        else:
            def rabinMiller(p):
                # Sayımız eğer asalsa True döner
                s = p - 1
                t = 0
                while s % 2 == 0:
                    s = s // 2  # s bitene kadar yarısını alacağız.
                    t += 1  # t'yi tutma nedeni ise s'nin kaç kere 2'ye bölünüdüğünü tutmak istememizdir.

                for trials in range(5):  # p değerinin asallığını 5 defa yanlışlamaya çalışacağız.
                    a = random.randrange(2, p - 1)
                    v = pow(a, s, p)
                    if v != 1:  # v, 1'e eşitse çalışmayacak
                        i = 0
                        while v != (p - 1):
                            if i == t - 1:
                                return False
                            else:
                                i = i + 1
                                v = (v ** 2) % p
                return True


            if rabinMiller(p) == True:
                P = p
                #print("p Asal Sayısı:", P)
                break
            else:
                p -= 1
    q = int(q)
    alfa_q = 10 * math.log(q, math.e)
    alfa_q = int(alfa_q)
    #print("alfa_q:",alfa_q)
    beta_q = q - alfa_q
    beta_q = int(beta_q)
    #print("beta_q:",beta_q)
    while q > beta_q:
        if q % 2 == 0:
            q -= 1
        else:
            def rabinMiller(q):
                # Sayımız eğer asalsa True döner
                s = q - 1
                t = 0
                while s % 2 == 0:
                    s = s // 2  # s bitene kadar yarısını alacağız.
                    t += 1  # t'yi tutma nedeni ise s'nin kaç kere 2'ye bölünüdüğünü tutmak istememizdir.

                for trials in range(5):  # q değerinin asallığını 5 defa yanlışlamaya çalışacağız.
                    a = random.randrange(2, q - 1)
                    v = pow(a, s, q)
                    if v != 1:  # v, 1'e eşitse çalışmayacak
                        i = 0
                        while v != (q - 1):
                            if i == t - 1:
                                return False
                            else:
                                i = i + 1
                                v = (v ** 2) % q
                return True


            if rabinMiller(q) == True:
                Q = q
                #print("q Asal Sayısı:", Q)
                break
            else:
                q -= 1

    N = P * Q
    #print("N:",N)
    #print(N.bit_length())
    if (N.bit_length() != bit):
        RSA()
    else:
        print("p Asal Sayısı:", P)
        print("q Asal Sayısı:", Q)
        print("N:", N)
        #print(N.bit_length())
    try:
        input("Press enter to continue")
    except traceback:
        pass
RSA()