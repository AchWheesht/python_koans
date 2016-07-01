print("Listing Primes")

prime_list = []
i = 0
while i < 10000:
    if i % 1000 == 0:
        print("Processed %d primes" % i)
    i += 1
    prime = True
    for n in range(i):
        if n != 0 and n!= 1 and n!= i:
            if i % n == 0: prime = False
    if prime == True:
        prime_list.append(i)

for i in range(10):
    count = 0
    for n in prime_list:
        if n == 0: continue
        if n % 10 == i: count += 1
    print("Number of primes ending in %d: %d" % (i, count))
            
