import math
from tabulate import tabulate
from matplotlib import pyplot as plt

student_id = [2, 5, 1, 5, 4, 0, 1]
porosity = 0.2 + 0.03 * student_id[6]
h = 70 - 7 * student_id[5]  #ft
p_b = 50 #psia
mu_o = 2.5 + 0.5 * student_id[5]  #cp
A = 640  #acres
S = 3 + 0.5 * student_id[6]
p_i = 5800  #psia
k = 5 + 3 * student_id[4]  #md
B_o = 1.05  #bbl/stb
c_t = 0.000040  #1/psi
r_w = 0.328  #ft
day = 30 + 2 * student_id[6]  #days
t = day * 24  #hours

J = ((k * h) /
     (162.6 * B_o * mu_o *
      (math.log10(t) + math.log10(k / (porosity * mu_o * c_t * (r_w ** 2)))
       - 3.23 + (0.87 * S))))  #STB/d-psi

q_0_at_p_b = J * (p_i - p_b)

my_data = [
    [p_b, q_0_at_p_b],
    [p_i, 0]
]

head = ["P_bhf (psi)", "q_0 (sb/day)"]
print(tabulate(my_data, headers=head, tablefmt="grid"))


x = [0, q_0_at_p_b]
y = [p_i, p_b]

plt.title('$p_{bhf}$ versus $q_{0}$ for the transient flow')
plt.xlabel('$q_{0}$ (STB/Day)', fontsize= 10)
plt.ylabel('$p_{bhf}$ (psia)', fontsize= 10)

plt.xlim([0, 2500])
plt.ylim([0, 6000])
plt.plot(x, y)
plt.show()


