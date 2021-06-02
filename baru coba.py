class tengu:
    def __init__(self):
        self.__nama = None
        self.__ukuran = '69'
        # self.__ya = print("chuaaaks")

    def set_nama(self, nama):
        self.__nama = nama

    def get_nama(self):
        return self.__nama

    def get_ukuran(self):
        return self.__ukuran

    def show(self, name):
        print('ANJING')

class coro(tengu):
    def show(self, name):
        print(name)

# tengu1 = tengu('boy', 'besar')
# tengu1
# print(tengu1.get_nama())

# data = {'hewan' : ['asu', 'celeng', 'babi'], 'suara' : ['pussy', 'bitch', 'uwuw', 'nggok']}
# for x in data:
#     a = x
#     for j in range(len(data[x])):
#         print(data[a][j], data[a][j])

# print(data['hewan'][1])

# print(tengu().get_ukuran())

