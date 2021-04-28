import random

a = 1
b = 1
c = 1
d = 1
y = 20

result = []

population = []
fitness_old = 0
fitness_new = 0
for i in range(5):
    population.append([])
    for j in range(4):
        population[i].append(random.choice(list(range(1, y//2+1))))

tick = 0
while True:
    print(population)
    live_coef = []
    for i in range(5):
        live_coef.append(abs(a*population[i][0] + b*population[i][1] + c*population[i][2] + d*population[i][3] - y))

    # check population
    for i in range(len(live_coef)):
        if live_coef[i] == 0:
            result = population[i]
            print("tick {}".format(tick+1))
            print("result")
            break
    if result != []: break

    fitness_new = sum(live_coef) / 5
    if fitness_old >= fitness_new:
        # do mutations
        print("mutate")
        nmut = random.choice(list(range(5)))
        for i in range(nmut):
            N = random.choice(list(range(4)))
            population[i][N] = random.choice(list(range(1, y//2+1)))
    fitness_old = fitness_new

    choice_probab = []
    temp = sum([1/i for i in live_coef])
    for i in range(5):
        choice_probab.append(1/live_coef[i]/temp)

    # chose parents and their genes
    parents = []
    for i in range(5):
        r1 = random.random()
        r2 = random.random()
        #print("choise probab: {}".format(choice_probab))
        #print("r1={}   r2={}".format(r1, r2))
        mom = []
        dad = []
        if r1>=0 and r1<= choice_probab[0]: mom = population[0]
        elif r1>choice_probab[0] and r1 <= sum(choice_probab[0:1]): mom = population[1]
        elif r1 > sum(choice_probab[0:1]) and r1 <= sum(choice_probab[0:2]): mom = population[2]
        elif r1 > sum(choice_probab[0:2]) and r1 <= sum(choice_probab[0:3]): mom = population[3]
        else: mom = population[4]

        if r2>=0 and r2 <= choice_probab[0]: dad = population[0]
        elif r2 > choice_probab[0] and r2 <= sum(choice_probab[0:1]): dad = population[1]
        elif r2 > sum(choice_probab[0:1]) and r2 <= sum(choice_probab[0:2]): dad = population[2]
        elif r2 > sum(choice_probab[0:2]) and r2 <= sum(choice_probab[0:3]): dad = population[3]
        else: dad = population[4]

        if mom == dad:
            if mom == population[4]: mom = population[0]
            elif mom == population[0]: mom = population[1]
            elif mom == population[1]: mom = population[2]
            elif mom == population[2]: mom = population[3]
            elif mom == population[3]: mom = population[4]

        nchanges = random.choice(list(range(0, 4)))
        mom_genes = []
        for i in range(nchanges):
            mom_genes.append(random.choice(list(range(0, 4))))
        parents.append([mom, dad, nchanges, mom_genes])

    #print("parents = {}".format(parents))
    new_population = []
    for i in range(5):
        new_population.append(parents[i][1])
        #print(new_population)
        for j in range(parents[i][2]):
            new_population[i][parents[i][3][j]] = parents[i][0][parents[i][3][j]]
        #print(new_population)

    population = new_population
    tick +=1

print(result)
