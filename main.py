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

    def setAnggota(self):
        for x in range (self.anggota - 1):
            self.nama.append(input("Nama anggota keluarga {} : ".format(x+2)))
            self.nikAnggota.append(int(input("Masukkan NIK {} : ".format(self.nama[x]))))

    def show(self):
        print("Nomer KK : {} \nKepala keluarga : {} \nNIK : {}".format(self.noKK, self.kepalaKeluarga, self.nik))
        for x in range (len(self.nikAnggota)):
            print()
            print("No KK : {} \nNama anggota keluarga : {} \nNIK : {}".format(self.noKK, self.nama[x], self.nikAnggota[x]))

# keluarga = dataKeluarga(int(input("Masukkan No KK : ")), input("Masukkan nama kepala keluarga : "), int(input("Masukkan NIK : ")), int(input("Masukkan total penghasilan : ")), input("Masukkan alamat : "))
# print()
# print(keluarga.show())

keluarga = anggotaKeluarga(int(input("No KK : ")), input("Nama kepala keluarga : "), int(input("NIK : ")), int(input("Total penghasilan : ")), input("Alamat : "), int(input("Jumlah anggota keluarga : ")))
keluarga.setAnggota()
print()
keluarga.show()