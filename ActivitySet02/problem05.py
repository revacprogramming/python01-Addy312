def get_cs():
    a = input("enter")
    return a
 
  

def cs_to_dict(cs):
    """convert connect string to a dictionary"""
    c = []
    d = cs.split(";")
    for i in d:
        c.append(tuple(i.split("=")))
    k=dict(c)
    return k


def dict_to_cs(d):
    """convert a dictionary to connect string"""
    e=d.items()
    f=list(e)
    for i in f:
        z="=".join(i)
        print(z,end=';')
    


def main():
    cs = get_cs()

    d = cs_to_dict(cs) # convert connect string to a dictionary
    print(d)

    cs = dict_to_cs(d)
    print(cs)


if _name_ == '_main_':
    main()