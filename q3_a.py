import math
from tabulate import tabulate
from matplotlib import pyplot as plt

student_id = [2, 5, 1, 5, 4, 0, 1]
porosity = 0.20 + 0.01 * student_id[6]
h = 20 + 2 * student_id[6] #ft
p_b = 2000 #psia
mu_o = 1 + (student_id[4] / 10) #cp
A = 600 #acres
S = 1.5 + 0.3 * student_id[6]
p_res = 3900 #psia
k = 8 + 2 * student_id[5] #md
B_o = 1.1 #bbl/stb
c_t = 0.00004 #1/psi
r_w = 0.328 #ft
r_e = 2980 #ft

J = ((k * h) /
     (141.2 * B_o * mu_o * (math.log(r_e / r_w) - 0.75 + S))) #STB/d-psi

q_bp = J * (p_res - p_b) #stb/day

q_v = (J * p_b) / 1.8

values_p_bhf = [0, 390, 2 * 390, 3 * 390, 4 * 390, 5 * 390]
values_q = []
for value in values_p_bhf:
    q = q_bp + q_v * (1 - 0.2 * (value / p_b) - 0.8 * ((value / p_b) ** 2))
    values_q.append(q)

my_data = [
    [0, values_q[0]],
    [values_p_bhf[1], values_q[1]],
    [values_p_bhf[2], values_q[2]],
    [values_p_bhf[3], values_q[3]],
    [values_p_bhf[4], values_q[4]],
    [values_p_bhf[5], values_q[5]],
    [p_b, q_bp],
    [p_res, 0]
]

head = ["P_bhf (psi)", "q_0 (sb/day)"]
print(tabulate(my_data, headers=head, tablefmt="grid"))

x = [values_q[0], values_q[1], values_q[2], values_q[3], values_q[4], values_q[5], q_bp, 0]
y = [0, values_p_bhf[1], values_p_bhf[2], values_p_bhf[3], values_p_bhf[4], values_p_bhf[5],
     p_b, p_res]

plt.title('$p_{bhf}$ versus $q_{0}$ for the unsaturated oil reservoir')
plt.xlabel('$q_{0}$ (STB/Day)', fontsize= 10)
plt.ylabel('$p_{bhf}$ (psia)', fontsize= 10)

plt.xlim([0, 500])
plt.ylim([0, 5000])
plt.plot(x, y)
plt.show()

