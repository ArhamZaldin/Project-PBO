class dataKeluarga:
    def __init__(self, noKK, kepalaKeluarga, nik, total, alamat):
        self.noKK = noKK
        self.kepalaKeluarga = kepalaKeluarga
        self.nik = nik
        self.total = total
        self.alamat = alamat

    def show(self):
        return "Nomer KK : {} \nKepala keluarga : {} \nNIK : {} \nTotal penghasilan : {} \nAlamat : {}".format(self.noKK, self.kepalaKeluarga, self.nik, self.total, self.alamat)

class anggotaKeluarga(dataKeluarga):
    def __init__(self, noKK, kepalaKeluarga, nik, total, alamat, anggota):
        super().__init__(noKK, kepalaKeluarga, nik, total, alamat)
        self.anggota = anggota
        self.nama = []
        self.nikAnggota = []

    def anggota(self):
        if self.anggota > 1 :
            for x in range(len(self.anggota - 1)):
                self.nama.append(input("Masukkan nama anggota keluarga {} : ".format(x)))
                self.nikAnggota.append(input("Masukkan NIK anggota keluarga {} : ".format(x)))

    def show(self):
        print("Nomer KK : {} \nNama anggota keluarga : {} \nNIK : {}".format(self.noKK, self.kepalaKeluarga, self.nik))
        for x in self.nikAnggota:
            return "No KK : {} \nNama anggota keluarga : {} \nNIK : {}".format(self.noKK, self.nama[x], self.nikAnggota[x])

keluarga = dataKeluarga(123, 'anto', 345, 1000000, 'Sumbersari')
print(keluarga.show())

# keluarga = anggotaKeluarga(123, 'anto', 345, 1000000, 'Sumbersari', 2)
# keluarga.anggota()
# print(keluarga.show)