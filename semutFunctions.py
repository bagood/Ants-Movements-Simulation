import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#ini update

class functions:
    def __init__(self, maxpher, n, probAnt):
        self.maxpher = maxpher
        self.n = n
        self.probAnt = probAnt
    
    def generate_matriks(self):
        matriks = np.array([np.array([10 for _ in range(self.n)]) for _ in range(self.n)])
        for i in range(0, self.n):
            for j in range(0, self.n):
                randNum = np.random.rand(1)
                if randNum < self.probAnt:
                    matriks[i, j] = 0
        init_feromone = np.linspace(10, self.maxpher+10, self.n)
        matriks[round(self.n/2)] = init_feromone
        return matriks

    def find_index_difusi(self, n_baris, n_sel, matriks):
        atas = [n_baris-1, n_sel]
        kanan = [n_baris, n_sel+1]
        bawah = [n_baris+1, n_sel]
        kiri = [n_baris, n_sel-1]
        list_tetangga = [atas, kanan, bawah, kiri]
        hasil_tetangga = []
        for tetangga in list_tetangga:
            if tetangga[0] >= 0 and tetangga[0] <= self.n - 1:
                if tetangga[1] >= 0  and tetangga[1] <= self.n - 1:
                    if matriks[tetangga[0], tetangga[1]] == 10 and matriks[tetangga[0], tetangga[1]] != 0:
                        hasil_tetangga.append(tetangga)
        return hasil_tetangga

    def difusi_feromone(self, diffusionRate, matriks, evaporate):
        ada_feromone = []
        for i in range(0,self.n):
            for j in range(0, self.n):
                if matriks[i, j] > 10:
                    ada_feromone.append([i, j])
        for i_fer in ada_feromone:
            tetangga = (1 - (4 * diffusionRate)) * matriks[i_fer[0], i_fer[1]]
            index_tetangga = functions.find_index_difusi(self, i_fer[0], i_fer[1], matriks)
            for index in index_tetangga:
                matriks[index[0], index[1]] = -1 * tetangga
        for i in range(0,self.n):
            for j in range(0, self.n):
                if matriks[i, j] > 10:
                    matriks[i, j] -= evaporate
                elif matriks[i ,j] < 0 :
                    matriks[i, j] *= -1
        return matriks

    def find_index_gerak_semut(self, n_baris, n_sel, matriks, n_dateng):
        atas = [n_baris-1, n_sel]
        kanan = [n_baris, n_sel+1]
        bawah = [n_baris+1, n_sel]
        kiri = [n_baris, n_sel-1]
        list_tetangga = [atas, kanan, bawah, kiri]
        list_tetangga_filtered = []
        hasil_tetangga = []
        for tetangga in list_tetangga:
            if tetangga[0] >= 0 and tetangga[0] <= self.n - 1:
                if tetangga[1] >= 0  and tetangga[1] <= self.n - 1:
                    list_tetangga_filtered.append(tetangga)
        for tetangga in list_tetangga_filtered:
            cell_tetangga = matriks[tetangga[0], tetangga[1]]
            if tetangga != n_dateng:
                if (cell_tetangga != 0) and (cell_tetangga > 10):
                    hasil_tetangga.append([tetangga, cell_tetangga])
        if hasil_tetangga == []:
            return False  
        index = 0
        max_fer = 0
        for hasil in hasil_tetangga:
            if hasil[1] > max_fer:
                index = hasil[0]
                max_fer = hasil[1]    
        return index

    def find_posisi_semut(self, matriks):
        posisi_semut = []
        for i in range(0,self.n):
            for j in range(0, self.n):
                if matriks[i, j] == 0:
                    posisi_semut.append([[i, j], None])
        return posisi_semut
    
    def pergerakan_semut(self, matriks, deposit, posisi_semut):
        for i, semut in enumerate(posisi_semut):
            koor = semut[0]
            arahGerak = functions.find_index_gerak_semut(self, koor[0], koor[1], matriks, semut[1])
            if arahGerak != False:
                matriks[arahGerak[0], arahGerak[1]] = 0
                matriks[koor[0], koor[1]] = deposit + 10
                posisi_semut[i][0] = arahGerak
                posisi_semut[i][1] = koor
        return (matriks, posisi_semut)
    




