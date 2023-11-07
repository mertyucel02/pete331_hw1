from tabulate import tabulate
from matplotlib import pyplot as plt

student_id = [2, 5, 1, 5, 4, 0, 1]
p_res = 3800 #psia
p_bp = 2200 #psia

#For Well A:

p_bhf_a = 3000 #psia
q_a_at_3000_psia = 620 + (student_id[5] * 8) #stb/day

J_a = q_a_at_3000_psia / (p_res - p_bhf_a) #stb/day-psi
q_bp_a = J_a * (p_res - p_bp) #stb/day

q_v_a = (J_a * p_bp) / 1.8

values_p_bhf_a = [0, 380, 2 * 380, 3 * 380, 4 * 380, 5 * 380]
values_q_a = []
for value_a in values_p_bhf_a:
    q_a = q_bp_a + q_v_a * (1 - 0.2 * (value_a / p_bp) - 0.8 * ((value_a / p_bp) ** 2))
    values_q_a.append(q_a)

my_data = [
    [0, values_q_a[0]],
    [values_p_bhf_a[1], values_q_a[1]],
    [values_p_bhf_a[2], values_q_a[2]],
    [values_p_bhf_a[3], values_q_a[3]],
    [values_p_bhf_a[4], values_q_a[4]],
    [values_p_bhf_a[5], values_q_a[5]],
    [p_bp, q_bp_a],
    [p_res, 0]
]

head = ["P_bhf (psi)", "q_0 (sb/day)"]
print(tabulate(my_data, headers=head, tablefmt="grid"))

x_a = [values_q_a[0], values_q_a[1], values_q_a[2], values_q_a[3], values_q_a[4], values_q_a[5], q_bp_a, 0]
y_a = [0, values_p_bhf_a[1], values_p_bhf_a[2], values_p_bhf_a[3], values_p_bhf_a[4], values_p_bhf_a[5],
     p_bp, p_res]

plt.title('IPR Graph for Well A')
plt.xlabel('$q_{0}$ (STB/Day)', fontsize= 10)
plt.ylabel('$p_{bhf}$ (psia)', fontsize= 10)

plt.xlim([0, 2300])
plt.ylim([0, 4000])
plt.plot(x_a, y_a)
plt.show()

#For Well B:

p_bhf_b = 1500 #psia
q_b_at_1500_psia = 880 + (student_id[6] * 12) #stb/day

J_b = q_b_at_1500_psia / ((p_res - p_bp) + (p_bp / 1.8) *
                          (1 - 0.2 * (p_bhf_b / p_bp)
                           - 0.8 * ((p_bhf_b / p_bp) ** 2))) #stb/day-psi
q_bp_b = J_b * (p_res - p_bp) #stb/day

q_v_b = (J_b * p_bp) / 1.8

values_p_bhf_b = [0, 380, 2 * 380, 3 * 380, 4 * 380, 5 * 380]
values_q_b = []
for value_b in values_p_bhf_b:
    q_b = q_bp_b + q_v_b * (1 - 0.2 * (value_b / p_bp) - 0.8 * ((value_b / p_bp) ** 2))
    values_q_b.append(q_b)

my_data = [
    [0, values_q_b[0]],
    [values_p_bhf_b[1], values_q_b[1]],
    [values_p_bhf_b[2], values_q_b[2]],
    [values_p_bhf_b[3], values_q_b[3]],
    [values_p_bhf_b[4], values_q_b[4]],
    [values_p_bhf_b[5], values_q_b[5]],
    [p_bp, q_bp_b],
    [p_res, 0]
]

head = ["P_bhf (psi)", "q_0 (sb/day)"]
print(tabulate(my_data, headers=head, tablefmt="grid"))

x_b = [values_q_b[0], values_q_b[1], values_q_b[2], values_q_b[3],
       values_q_b[4], values_q_b[5], q_bp_b, 0]
y_b = [0, values_p_bhf_b[1], values_p_bhf_b[2], values_p_bhf_b[3], values_p_bhf_b[4], values_p_bhf_b[5],
     p_bp, p_res]

plt.title('IPR Graph for Well B')
plt.xlabel('$q_{0}$ (STB/Day)', fontsize= 10)
plt.ylabel('$p_{bhf}$ (psia)', fontsize= 10)

plt.xlim([0, 2300])
plt.ylim([0, 4000])
plt.plot(x_b, y_b)
plt.show()

