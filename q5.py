from tabulate import tabulate
from matplotlib import pyplot as plt

student_id = [2, 5, 1, 5, 4, 0, 1]
p_bp = 50 #psia
p_layer_1 = 2500 #psia
p_layer_2 = 2120 + (student_id[5] * 3) #psia
p_layer_3 = 2700 #psia

J_layer_1 = 0.3 #stb/d-psia
J_layer_2 = 1 #stb/d-psia
J_layer_3 = 0.6 #stb/d-psia

p_bhf = 1750 + (student_id[6] * 50) #psia

values_p_bhf = [p_bp, p_bhf, 2120, 2363.157895]
values_q_layer_1 = []
values_q_layer_2 = []
values_q_layer_3 = []
values_q_tot = []
for value in values_p_bhf:
    q_layer_1 = J_layer_1 * (p_layer_1 - value)
    values_q_layer_1.append(q_layer_1)
    q_layer_2 = J_layer_2 * (p_layer_2 - value)
    values_q_layer_2.append(q_layer_2)
    q_layer_3 = J_layer_3 * (p_layer_3 - value)
    values_q_layer_3.append(q_layer_3)
    q_tot = q_layer_1 + q_layer_2 + q_layer_3
    values_q_tot.append(q_tot)

str1 = str(p_bhf)
my_data = [
    ["Layer 1", values_q_layer_1[0], values_q_layer_1[1],
     values_q_layer_1[2], values_q_layer_1[3]],
    ["Layer 2", values_q_layer_2[0], values_q_layer_2[1],
     values_q_layer_2[2], values_q_layer_2[3]],
    ["Layer 3", values_q_layer_3[0], values_q_layer_3[1],
     values_q_layer_3[2], values_q_layer_3[3]],
    ["Total Rate", values_q_tot[0], values_q_tot[1],
     values_q_tot[2], int(values_q_tot[3])]
]

head = ["Layer", "50 psia", str1 + " psia", "2120 psia", "2363.157895 psia"]
print(tabulate(my_data, headers=head, tablefmt="grid"))

x_1 = [values_q_layer_1[0], values_q_layer_1[1], values_q_layer_1[2], values_q_layer_1[3]]
y_1 = [p_bp, p_bhf, 2120, 2363.157895]

x_2 = [values_q_layer_2[0], values_q_layer_2[1], values_q_layer_2[2], values_q_layer_2[3]]
y_2 = [p_bp, p_bhf, 2120, 2363.157895]

x_3 = [values_q_layer_3[0], values_q_layer_3[1], values_q_layer_3[2], values_q_layer_3[3]]
y_3 = [p_bp, p_bhf, 2120, 2363.157895]

x_tot = [values_q_tot[0], values_q_tot[1], values_q_tot[2], int(values_q_tot[3])]
y_tot = [p_bp, p_bhf, 2120, 2363.157895]

plt.title('IPR Graph for each layer and the composite IPR')
plt.xlabel('$q_{0}$ (STB/Day)', fontsize= 10)
plt.ylabel('$p_{bhf}$ (psia)', fontsize= 10)
plt.plot(x_1, y_1, label= "Layer 1")
plt.plot(x_2, y_2, label= "Layer 2")
plt.plot(x_3, y_3, label= "Layer 3")
plt.plot(x_tot, y_tot, label= "Total Rate", linestyle= "--")
plt.legend()
plt.show()




