from storeFunctions import functions
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns

# Initiate all the variables for the simulation
maxpher = 50
n = 17
probAnt = 0.1
evaporate = 1
deposit = 2
threshold = 50
diffusionRate = 0.01
iter = 50

# Generates each iterations for the simulation 
funcSemut = functions(maxpher, n, probAnt)
list_matriks = np.zeros((iter, 17, 17))
matriks = funcSemut.generate_matriks()
posisi_semut = funcSemut.find_posisi_semut(matriks)

list_matriks[0] = matriks
for i in range(1, iter):
    matriks, posisi_semut = funcSemut.pergerakan_semut(matriks, deposit, posisi_semut)
    matriks = funcSemut.difusi_feromone(diffusionRate, matriks, evaporate)
    list_matriks[i] = matriks

# Visualize the simulation
def init():
    plt.clf()
    return None

def animate(i):
    plt.clf()
    ax = sns.heatmap(list_matriks[i],
                    square=True,
                    xticklabels=False,
                    yticklabels=False)
    return None

fig = plt.figure()
anim = animation.FuncAnimation(fig,
                               animate,
                               frames=range(0, iter, 1),
                               blit=False,
                               interval=50,
                               init_func=init)  
plt.show()