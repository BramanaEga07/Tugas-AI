#SISTEM PERJALANAN KRL DI JABODETABEK#

graf =  {'JakartaKota':set(['Manggarai','Duri']),
         'Manggarai':set(['JakartaKota','Jatinegara','Bogor']),
         'Jatinegara':set(['Rajawali','Manggarai','Bekasi']),
         'Rajawali':set(['KampungBandan','Jatinegara']),
         'KampungBandan':set(['Rajawali','Duri']),
         'Duri':set(['KampungBandan','JakartaKota','TanahAbang']),
         'TanahAbang':set(['Duri','Bogor']),
         'Bogor':set(['Manggarai','TanahAbang','Bekasi']),
         'Bekasi':set(['Jatinegara','Bogor'])}

def bfs(graf, mulai, tujuan):
    queue = [[mulai]]
    visited = set()

    while queue:     
        
        jalur = queue.pop(0)
 
        state = jalur[-1]

        if state == tujuan:
            return jalur
        
        elif state not in visited:
            
            for cabang in graf.get(state, []): 
                jalur_baru = list(jalur) 
                jalur_baru.append(cabang) 
                queue.append(jalur_baru) 

            visited.add(state)

        isi = len(queue)
        if isi == 0:
            print("Tidak ditemukan")

print (bfs(graf,'JakartaKota','Bekasi'))
