class dataKeluarga:
    def __init__(self, noKK, kepalaKeluarga, nik, total, alamat):
        self.noKK = noKK
        self.kepalaKeluarga = kepalaKeluarga
        self.nik = nik
        self.total = total
        self.alamat = alamat

    def show(self):
        return

class anggotaKeluarga(dataKeluarga):
    def __init__(self, noKK, kepalaKeluarga, nik, total, alamat, anggota):
        super().__init__(noKK, kepalaKeluarga, nik, total, alamat)
        self.anggota = anggota

    def anggota(self):
        if self.anggota > 1 :
            for x in range (len(self.anggota - 1)):


    def show(self):
        return

