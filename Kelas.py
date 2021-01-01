import sqlite3

class database:
    def __init__(self):
        self.conn = sqlite3.connect('bantuanWarga.db')
        self.cursor = self.conn.cursor()

    def executeQuery(self, query, retVal=False):
        res = self.cursor.execute(query)
        results = res.fetchall()
        self.conn.commit()
        if retVal:
            return results

    def checkVal(self, query):
        res = self.cursor.execute(query)
        return res.fetchone()

    def close(self):
        self.conn.close()

class dataKeluarga(database):
    def setKeluarga(self, noKK, kepalaKeluarga, anggota, total, alamat):
        self.executeQuery("CREATE TABLE IF NOT EXISTS Keluarga (noKK int primary key, kepalaKeluarga varchar, anggotaKeluarga int, totalPendapatan float, alamat varchar)")
        query = f"SELECT * FROM Keluarga WHERE noKK = '{noKK}'"
        check = self.checkVal(query)
        if check is None:
            query2 = f"INSERT INTO Keluarga VALUES ('{noKK}', '{kepalaKeluarga}', '{anggota}', '{total}', '{alamat}')"
            self.executeQuery(query2)
            print(f"Sdr/i {kepalaKeluarga} berhasil didaftarkan sebagai kepala keluarga.")
        else:
            print(f"Nomor KK {noKK} sudah ada!")

    def showKeluarga(self):
        list = self.executeQuery("SELECT * FROM Keluarga ORDER BY kepalaKeluarga", True)
        for row in list:
            print(f' \t\t {row[0]} \t\t {row[1]} \t\t\t {row[2]} \t\t\t\t {row[3]} \t\t {row[4]}')

    def readByTotalBelow(self, total):
        query = f"SELECT * FROM Keluarga WHERE totalPendapatan < '{total}' ORDER BY kepalaKeluarga"
        list = self.executeQuery(query, True)
        for row in list:
            print(f' \t\t {row[0]} \t\t {row[1]} \t\t\t {row[2]} \t\t\t\t {row[3]} \t\t {row[4]}')

    def readByTotalAbove(self, total):
        query = f"SELECT * FROM Keluarga WHERE totalPendapatan > '{total}' ORDER BY kepalaKeluarga"
        list = self.executeQuery(query, True)
        for row in list:
            print(f' \t\t{row[0]} \t\t {row[1]} \t\t\t {row[2]} \t\t\t\t {row[3]} \t\t {row[4]}')

    def readByAnggotaBelow(self, anggota):
        query = f"SELECT * FROM Keluarga WHERE anggotaKeluarga < '{anggota}' ORDER BY kepalaKeluarga"
        list = self.executeQuery(query, True)
        for row in list:
            print(f' \t\t {row[0]} \t\t {row[1]} \t\t\t {row[2]} \t\t\t\t {row[3]} \t\t {row[4]}')

    def readByAnggotaAbove(self, anggota):
        query = f"SELECT * FROM Keluarga WHERE anggotaKeluarga > '{anggota}' ORDER BY kepalaKeluarga"
        list = self.executeQuery(query, True)
        for row in list:
            print(f' \t\t {row[0]} \t\t {row[1]} \t\t\t {row[2]} \t\t\t\t {row[3]} \t\t {row[4]}')

    def updateTotalPendapatan(self, noKK, total):
        query = f"SELECT * FROM Keluarga WHERE noKK = '{noKK}'"
        check = self.checkVal(query)
        if check is not None:
            query2 = f"UPDATE Keluarga SET totalPendapatan = '{total}' WHERE noKK = '{noKK}'"
            self.executeQuery(query2)
            print(f"Total pendapatan berhasil diubah menjadi {total}.")
        else:
            print(f"Nomor KK {noKK} tidak ditemukan!")

    def updateAlamat(self, noKK, alamat):
        query = f"SELECT * FROM Keluarga WHERE noKK = '{noKK}'"
        check = self.checkVal(query)
        if check is not None:
            query2 = f"UPDATE Keluarga SET alamat = '{alamat}' WHERE noKK = '{noKK}'"
            self.executeQuery(query2)
            print(f"Alamat berhasil diubah menjadi {alamat}.")
        else:
            print(f"Nomor KK {noKK} tidak ditemukan!")

    def delKeluarga(self, noKK):
        query = f"SELECT * FROM Keluarga WHERE noKK = '{noKK}'"
        check = self.checkVal(query)
        if check is not None:
            query2 = f"DELETE FROM Keluarga WHERE noKK = '{noKK}'"
            query3 = f"DELETE FROM Anggota_Keluarga WHERE noKK = '{noKK}'"
            self.executeQuery(query2)
            self.executeQuery(query3)
            print(f"Data keluarga dengan Nomor KK {noKK} berhasil dihapus!")
        else:
            print(f"Nomor KK {noKK} tidak ditemukan!")

    def searchDetailKeluarga(self, noKK):
        query = f"SELECT * FROM Keluarga WHERE noKK = '{noKK}'"
        check = self.checkVal(query)
        list = self.executeQuery(query, True)
        if check is not None:
            print("""
            ~ ~ DATA KELUARGA ~ ~
            ---------------------
            """)
            for row in list:
                print(f'Nomer KK : {row[0]} \nKepala Keluarga : {row[1]} \nJumlah anggota keluarga : {row[2]} \nTotal pendapatan : {row[3]} \nAlamat : {row[4]}')
                print()

            query2 = f"SELECT * FROM Anggota_Keluarga WHERE noKK = '{noKK}'"
            list2 = self.executeQuery(query2, True)
            print("""
            ~ ~ ~ ANGGOTA KELUARGA ~ ~ ~
            ----------------------------
            """)
            for rows in list2:
                print(f'NIK : {rows[0]} \nNama : {rows[1]}')
                print()
        else:
            print(f"Nomor KK {noKK} tidak ditemukan!")

class anggotaKeluarga(dataKeluarga):
    def addKeluarga(self, noKK, kepalaKeluarga, anggota, total, alamat, nik):
        self.setKeluarga(noKK, kepalaKeluarga, anggota, total, alamat)
        self.executeQuery("CREATE TABLE IF NOT EXISTS Anggota_Keluarga (NIK int primary key, nama varchar, noKK int, foreign key(noKK) REFERENCES Keluarga(noKK))")
        query = f"INSERT INTO Anggota_Keluarga VALUES ('{nik}', '{kepalaKeluarga}', '{noKK}')"
        self.executeQuery(query)

    def setAnggota(self, nikAnggota, nama, noKK):
        query = f"SELECT * FROM Keluarga WHERE noKK = '{noKK}'"
        check = self.checkVal(query)
        if check is not None:
            query2 = f"SELECT * FROM Anggota_Keluarga WHERE NIK = '{nikAnggota}'"
            check2 = self.checkVal(query2)
            if check2 is None:
                query3 = f"INSERT INTO Anggota_Keluarga VALUES ('{nikAnggota}', '{nama}', '{noKK}')"
                self.executeQuery(query3)
                print(f"Sdr/i {nama} berhasil didaftarkan sebagai anggota keluarga")
                return False
            else:
                print(f"NIK {nikAnggota} sudah ada!")
        else:
            print(f"Nomor KK {noKK} tidak ditemukan!")

    def showKeluarga(self, noKK, kepalaKeluarga, anggota, total, alamat, nik):
        print()
        print(f"Nomer KK : {noKK} \nKepala keluarga : {kepalaKeluarga} \nNIK : {nik} \nJumlah anggota keluarga : {anggota} \nTotal pendapatan : {total} \nAlamat : {alamat}")

    def showAnggota(self, nikAnggota, nama):
        print()
        print(f"Nama anggota keluarga : {nama} \nNIK : {nikAnggota}")

    def delKeluarga(self, noKK):
        query = f"DELETE FROM Keluarga WHERE noKK = '{noKK}'"
        query2 = f"DELETE FROM Anggota_Keluarga WHERE noKK = '{noKK}'"
        self.executeQuery(query)
        self.executeQuery(query2)

    def delAnggota(self, noKK, nikAnggota):
        query = f"SELECT * FROM Anggota_Keluarga WHERE noKK = '{noKK}' and NIK = '{nikAnggota}'"
        check = self.checkVal(query)
        if check is not None:
            query2 = f"DELETE FROM Anggota_Keluarga WHERE NIK = '{nikAnggota}'"
            self.executeQuery(query2)
            print(f"Anggota keluarga dengan NIK {nikAnggota} berhasil dihapus!")
        else:
            print(f"Nomer KK {noKK} atau NIK {nikAnggota} tidak ditemukan!")

    def updateAnggota(self, noKK):
        query = f"SELECT count(*) FROM Anggota_Keluarga WHERE noKK = '{noKK}'"
        list = self.executeQuery(query, True)
        for row in list:
            query2 = f"UPDATE Keluarga SET anggotaKeluarga = '{row[0]}' WHERE noKK = '{noKK}'"
            self.executeQuery(query2)

class bantuan(database):
    def __init__(self, umr):
        super().__init__()
        self.umr = umr

    def analyze(self):
        query = f"SELECT * FROM Keluarga WHERE totalPendapatan <= '{self.umr}'"
        list = self.executeQuery(query, True)
        anggota = []
        limit = []
        z = 0
        for row in list:
            anggota.append(row[2])
            limit.append(float(self.umr - row[3]))
        for x in range(len(anggota)):
            if anggota[x] > 1:
                for y in range(anggota[x] - 1):
                    limit[x] += 100000
        for rows in list:
            print(f' \t {rows[0]} \t\t {rows[1]} \t\t {rows[4]} \t\t {limit[z]}')
            z += 1

class rekap(database):
    def catatBantuan(self, noKK, donations):
        self.executeQuery("CREATE TABLE IF NOT EXISTS Rekap_Data (idRekap INTEGER PRIMARY KEY, noKK int, bantuan float, FOREIGN KEY(noKK) references Keluarga(noKK))")
        query = f"SELECT * FROM Keluarga WHERE noKK = '{noKK}'"
        check = self.checkVal(query)
        if check is not None:
            query2 = f"INSERT INTO Rekap_Data VALUES (null, '{noKK}', '{donations}')"
            self.executeQuery(query2)
            print("Data berhasil direkap!")
        else:
            print(f"Nomer KK {noKK} belum terdaftar!")

    def riwayatBantuan(self):
        list = self.executeQuery("SELECT * FROM Rekap_Data", True)
        check = self.checkVal("SELECT * FROM Rekap_Data")
        if check is not None:
            for row in list:
                print(f' \t\t{row[0]} \t {row[1]} \t\t {row[2]}')
        else:
            print("~ ~ DATA KOSONG ~ ~")

######## BATAS CLASS ########

def addDataKeluarga():
    print("""
    ---------------------------------
    ~ ~ Menambahkan data keluarga ~ ~
    ---------------------------------
    """)
    noKK = int(input("Nomer KK : "))
    kepalaKeluarga = str(input("Nama kepala keluarga : "))
    nik = int(input("NIK : "))
    anggota = int(input("Jumlah anggota keluarga : "))
    total = float(input("Total pendapatan : "))
    alamat = str(input("Alamat : "))
    nama = []
    nikAnggota = []
    keluarga = anggotaKeluarga()
    keluarga.addKeluarga(noKK, kepalaKeluarga, anggota, total, alamat, nik)
    for x in range (anggota - 1):
        tryAgain = True
        while tryAgain:
            nama.append(str(input(f"Nama anggota keluarga {x+2} : ")))
            nikAnggota.append(int(input(f"Masukkan NIK {nama[x]} : ")))
            tryAgain = keluarga.setAnggota(nikAnggota[x], nama[x], noKK)
    keluarga.showKeluarga(noKK, kepalaKeluarga, anggota, total, alamat, nik)
    for y in range (len(nama)):
        keluarga.showAnggota(nikAnggota[y], nama[y])
    print("""
    Data sudah benar?
    1.YA   2.TIDAK
    """)
    option = input("Masukkan pilihan : ")
    if option == '1':
        pass
    elif option == '2':
        keluarga.delKeluarga(noKK)
    else:
        print("Masukkan pilihan dengan benar!")

def showDataKeluarga():
    print("""
    -----------------------------
    ~ ~ Melihat data keluarga ~ ~
    -----------------------------
    Filter :
        1. Tidak ada
        2. Total pendapatan kurang dari ...
        3. Total pendapatan lebih dari ...
        4. Anggota keluarga kurang dari ...
        5. Anggota keluarga lebih dari ...
    """)
    option = input("Masukkan pilihan : ")

    if option == '1':
        print("""
        Nomor KK   Kepala Keluarga   Anggota Keluarga   Total Pendapatan   Alamat
        ===========================================================================
        """)
        keluarga = dataKeluarga()
        keluarga.showKeluarga()
    elif option == '2':
        pendapatan = float(input("Total pendapatan kurang dari : "))
        print("""
        Nomor KK   Kepala Keluarga   Anggota Keluarga   Total Pendapatan   Alamat
        ===========================================================================
        """)
        keluarga = dataKeluarga()
        keluarga.readByTotalBelow(pendapatan)
    elif option == '3':
        pendapatan = float(input("Total pendapatan lebih dari : "))
        print("""
        Nomor KK   Kepala Keluarga   Anggota Keluarga   Total Pendapatan   Alamat
        ===========================================================================
        """)
        keluarga = dataKeluarga()
        keluarga.readByTotalAbove(pendapatan)
    elif option == '4':
        anggota = int(input("Anggota keluarga kurang dari : "))
        print("""
        Nomor KK   Kepala Keluarga   Anggota Keluarga   Total Pendapatan   Alamat
        ===========================================================================
        """)
        keluarga = dataKeluarga()
        keluarga.readByAnggotaBelow(anggota)
    elif option == '5':
        anggota = int(input("Anggota keluarga lebih dari : "))
        print("""
        Nomor KK   Kepala Keluarga   Anggota Keluarga   Total Pendapatan   Alamat
        ===========================================================================
        """)
        keluarga = dataKeluarga()
        keluarga.readByAnggotaAbove(anggota)
    else:
        print("Masukkan pilihan dengan benar!")

def changeDataKeluarga():
    print("""
    ------------------------------
    ~ ~ Mengubah data keluarga ~ ~
    ------------------------------
    Submenu :
        1. Ubah data
        2. Hapus data
    """)
    option = input("Masukkan pilihan : ")
    if option == '1':
        print("""
        -----------------
        ~ ~ Ubah data ~ ~
        -----------------
        Submenu :
            1. Ubah total pendapatan
            2. Ubah alamat
            3. Tambah anggota keluarga
        """)
        option2 = input("Masukkan pilihan : ")
        if option2 == '1':
            noKK = int(input("Masukkan nomer KK : "))
            total = float(input("Total pendapatan baru : "))
            keluarga = dataKeluarga()
            keluarga.updateTotalPendapatan(noKK, total)
        elif option2 == '2':
            noKK = int(input("Masukkan nomer KK : "))
            alamat = input("Masukkan alamat baru : ")
            keluarga = dataKeluarga()
            keluarga.updateAlamat(noKK, alamat)
        elif option2 == '3':
            noKK = int(input("Masukkan nomer KK : "))
            anggota = int(input("Jumlah anggota keluarga yang ingin ditambahkan : "))
            nama = []
            nikAnggota = []
            keluarga = anggotaKeluarga()
            for x in range(anggota):
                tryAgain = True
                while tryAgain:
                    nama.append(input(f"Nama anggota baru {x + 1} : "))
                    nikAnggota.append(int(input(f"Masukkan NIK {nama[x]} : ")))
                    tryAgain = keluarga.setAnggota(nikAnggota[x], nama[x], noKK)
            keluarga.updateAnggota(noKK)
        else:
            print("Masukkan pilihan dengan benar!")

    elif option == '2':
        print("""
        ------------------
        ~ ~ Hapus data ~ ~
        ------------------
        Submenu :
            1. Hapus data keluarga
            2. Hapus data anggota keluarga
        """)
        option2 = input("Masukkan pilihan : ")
        if option2 == '1':
            keluarga = dataKeluarga()
            keluarga.delKeluarga(int(input("Masukkan nomor KK : ")))
        elif option2 == '2':
            noKK = int(input("Masukkan nomer KK : "))
            nik = int(input("Masukkan NIK : "))
            keluarga = anggotaKeluarga()
            keluarga.delAnggota(noKK, nik)
            keluarga.updateAnggota(noKK)
        else:
            print("Masukkan pilihan dengan benar!")
    else:
        print("Masukkan pilihan dengan benar!")

def searchDetail():
    print("""
    ------------------------------------
    ~ ~ Mencari detail data keluarga ~ ~
    ------------------------------------
    """)
    keluarga = dataKeluarga()
    keluarga.searchDetailKeluarga(int(input("Masukkan nomor KK : ")))

def recommend():
    print("""
    ---------------------------
    ~ ~ Rekomendasi bantuan ~ ~
    ---------------------------
    """)
    dana = bantuan(float(input("Masukkan UMR : ")))
    print("""
    Nomer KK    Kepala Keluarga         Alamat      Saran Bantuan
    ===============================================================
    """)
    dana.analyze()

def rekapDana():
    print("""
    --------------------------
    ~ ~ Rekap Dana Bantuan ~ ~
    --------------------------
    Submenu :
        1. Catat pemberian bantuan
        2. Riwayat pemberian bantuan
    """)
    option = input("Masukkan pilihan : ")
    if option == '1':
        noKK = int(input("Masukkan nomer KK : "))
        donations = float(input("Dana yang telah diberikan : "))
        data = rekap()
        data.catatBantuan(noKK, donations)
    elif option == '2':
        print("""
        -----------------------
        ~ ~ Riwayat Bantuan ~ ~
        -----------------------
        ID   Nomer KK     Bantuan
        ==========================
        """)
        data = rekap()
        data.riwayatBantuan()
    else:
        print("Masukkan pilihan dengan benar!")

def exit():
    print("""
    ------------
    ~ ~ EXIT ~ ~
    ------------
    """)
    database().close()

def Menu():
    print("""
    |======================================|
    |     ~ ~ ~ Selamat Datang ~ ~ ~       |
    |                                      |
    |    Menu Utama                        |
    |    1. Menambahkan data keluarga      |
    |    2. Melihat data keluarga          |
    |    3. Mengubah data keluarga         |
    |    4. Mencari detail data keluarga   |
    |    5. Rekomendasi bantuan            |
    |    6. Rekap dana bantuan             |
    |    7. Exit                           |
    |======================================|
    """)

######## BATAS MENU ########

while True:
    Menu()
    menu = input("Masukkan nomor menu : ")
    if menu == '1':
        addDataKeluarga()
    elif menu == '2':
        showDataKeluarga()
    elif menu == '3':
        changeDataKeluarga()
    elif menu == '4':
        searchDetail()
    elif menu == '5':
        recommend()
    elif menu == '6':
        rekapDana()
    elif menu == '7':
        exit()
        break
    else:
        print("Masukkan pilihan dengan benar!")
        database().close()
        break