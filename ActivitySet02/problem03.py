

def get_cs():
    a=input("Enter string")
    return a
  

def cs_to_lot(cs):
  split=tuple(cs.split(),cs[0])
  l=list(split)
  return l
  


def main():
    cs = get_cs()

    lot = cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main()
