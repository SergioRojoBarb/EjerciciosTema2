
class lista:
    def __init__(self, list):
        self.list = list

    def mod(self):
        l = []
        let = 0
        let2 = 0
        i = 0
        for n in self.list:
            for t in self.list:
                if n == t:
                    let += 1
                    if let > 1:
                        break
                    l.append(n)
            let = 0
        for r in l:
            for p in l:
                if r == p:
                    let2 += 1
                    if let2 > 1:
                        l.pop(i)
            i += 1
            let2 = 0
        return l

    def orden(self):
        sl = self.list
        sl.sort(reverse=True)
        return sl

    def delete(self):
        par = []
        self.list.sort()
        for num in self.list:
            if num%2 == 0:
                par.append(num)
        return par

    def sum(self):
        return sum(self.mod())

    def add(self):
        list_ad=self.mod()
        list_ad.insert(0, self.sum())
        return list_ad


list = [1,2,8,3,5,9,4,6,7]
l0= mod_list(list)



                    
