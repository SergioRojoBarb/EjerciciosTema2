
lista = [972, -15, 92, 45, -33, 209, 394, 1, 5, 3, 3, -38, 40, 27, 67]

#a = sum(lista)
#print(a)

def modificar(t):
    t = list(set(1)) #dupl
    t.sort(reverse=True) #may a men
    t_par = []

    for n in t:
        if n%2 == 0:
            t_par.append(n)
    
    s = sum(t_par)
    t_par.insert(0, s)
    return t_par  

mod_t = modificar(lista)

print(mod_t[0] == sum(mod_t[1:]))

