def finn_primtall_mellom_tallene(tall1, tall2):
    for i in range(tall1, tall2+1):
        if i % 2 == 0:
            print(i)

finn_primtall_mellom_tallene(1, 1000)