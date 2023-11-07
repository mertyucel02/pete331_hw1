import math
from tabulate import tabulate
from matplotlib import pyplot as plt

student_id = [2, 5, 1, 5, 4, 0, 1]
porosity = 0.25 + (student_id[4] / 100)
h = 22 + 3 * student_id[5] #ft
p_b = 4200 #psia
mu_o = 0.5 + (student_id[6] / 5) #cp
A = 600 #acres
S = 2 + 3 * student_id[6]
p_res = 4200 #psia
k = 15 + student_id[5] #md
B_o = 1.2 #bbl/stb
c_t = 0.00003 #1/psi
r_w = 0.328 #ft


acre_to_sq_ft = A * 43560 #ft^2

r_e = math.sqrt(acre_to_sq_ft / math.pi)

J = ((k * h) /
     (141.2 * B_o * mu_o * (math.log(r_e / r_w) - 0.75 + S))) #STB/d-psi

q_max = (J * p_res) / 1.8 #stb/day

values_p_bhf = [4000, 3500, 3000, 2500, 2000, 1500, 1000, 500]
values_q = []
for value in values_p_bhf:
    q = q_max * (1 - 0.2 * (value / p_res) - 0.8 * ((value / p_res)**2))
    values_q.append(q)

my_data = [
    [p_res, 0],
    [values_p_bhf[0], values_q[0]],
    [values_p_bhf[1], values_q[1]],
    [values_p_bhf[2], values_q[2]],
    [values_p_bhf[3], values_q[3]],
    [values_p_bhf[4], values_q[4]],
    [values_p_bhf[5], values_q[5]],
    [values_p_bhf[6], values_q[6]],
    [values_p_bhf[7], values_q[7]],
    [0, q_max]
]

head = ["P_bhf (psi)", "q_0 (sb/day)"]
print(tabulate(my_data, headers=head, tablefmt="grid"))

x = [0, values_q[0], values_q[1], values_q[2], values_q[3], values_q[4],
     values_q[5], values_q[6], values_q[7], q_max]
y = [p_res, values_p_bhf[0], values_p_bhf[1], values_p_bhf[2], values_p_bhf[3],
     values_p_bhf[4], values_p_bhf[5], values_p_bhf[6], values_p_bhf[7], 0]

plt.title('$p_{bhf}$ versus $q_{0}$ for the pseudo - steady - state flow')
plt.xlabel('$q_{0}$ (STB/Day)', fontsize= 10)
plt.ylabel('$p_{bhf}$ (psia)', fontsize= 10)

plt.xlim([0, 500])
plt.ylim([0, 5000])
plt.plot(x, y)
plt.show()




