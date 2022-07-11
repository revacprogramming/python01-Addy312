def get_cs():
    a = input("enter")
    return a


def cs_to_lot(cs):
    d=''
    c = []
    d = cs.split(";")
    for i in d:
        c.append(tuple(i.split("=")))
    return c


def lot_to_cs(cs_to_lot):
    for i in cs_to_lot:
        b = "=".join(i)
        print(b, end=';')


def main():
    cs = get_cs()

    lot = cs_to_lot(cs)  # convert connect string to list of tuples


    lot_to_cs(lot)  # convert list of strings to connect string





if _name_ == '_main_':
    main()