class Nut:
    def __init__(self, khoa=None):
        self.khoa = khoa
        self.trai = None
        self.phai = None
    # def

    def chen(seft, khoa):
        if seft is None:
            nut = Nut(khoa)
            seft = nut
            return
        # if

        if khoa < seft.khoa:
            if seft.trai == None:
                seft.trai = Nut(khoa)
            else:
                seft.trai.chen(khoa)
        elif khoa >self.khoa:
            if self.phai == None:
                seft.phai = Nut(khoa)
            else:
                seft.phai.chen(khoa)
        else:
            print(f"Nut bi trung")
    #def
#class

class CayNhiPhanTimKiem:
    def __init__(self, khoa=None):
        if khoa == None:
            self.goc = None
        else:
            self.goc = Nut(khoa)
        #if
    #def

    def chen(self, khoa):
        if self.goc == Node: