import random

x, y = 1.0, 1.0
delta = 2.0
n_trials = 2**16
n_hits = 0
n_inside = 0
n_outside = 0
for i in range(n_trials):
    del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
    if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
        x, y = x + del_x, y + del_y
        n_inside += 1
    else:
        n_outside += 1
    if x**2 + y**2 < 1.0: n_hits += 1
print (4.0 * n_hits / float(n_trials))
print("n_inside ", n_inside)
print("aceptance rate: ", n_inside/float(n_trials))

# delta | acceptance rate
# 0.062 | 0.966
# 0.125 | 0.94
# 0.25  | 0.878
# 0.5   | 0.766
# 1.0   | 0.559
# 2.0   | 0.250
# 4.0   |