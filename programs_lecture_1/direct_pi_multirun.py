import random
 
def direct_pi(N):
    n_hits = 0
    for i in range(N):
        x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
        if x ** 2 + y ** 2 < 1.0:
            n_hits += 1
    return n_hits
 
n_runs = 1000
n_trials = 4000

# guardar el valor de pi en cada corrida
pi_vector = []
for run in range(n_runs):
    pi_k = 4.0 * direct_pi(n_trials) / float(n_trials)
    print(run, pi_k)
    pi_vector.append(pi_k)

# guardar el valor promedio de pi
pi_mean = sum(pi_vector) / float(n_runs)    
print("Promedio de pi: ", pi_mean)
