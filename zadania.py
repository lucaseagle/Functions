def kodpocz (s1, s2):
    a = list(map(lambda x: int(x.replace('-', '')), [s1,s2]))
    return ['-'.join([str(i//1000), str(i%1000)]) for i in range(a[0]+1, a[1])]


def missing(lista, n):
    return sorted(list(((set(list(range(1, n+1))) - set(lista)))))


def halfjump(n1, n2):
    x = []
    while n1<=n2:
        x.append(float(n1))
        n1+=0.5
    return x