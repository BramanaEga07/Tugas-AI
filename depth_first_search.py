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

   

def dfs(graf, mulai, tujuan):
    stack = [[mulai]]
    visited = set()

    while stack:
        panjang_tumpukan = len(stack)-1
               
        jalur = stack.pop(panjang_tumpukan)
 
        state = jalur[-1]

        if state == tujuan:
            return jalur
        
        elif state not in visited:
            
            for cabang in graf.get(state, []): 
                jalur_baru = list(jalur) 
                jalur_baru.append(cabang) 
                stack.append(jalur_baru) 
            
            visited.add(state)

        isi = len(stack)
        if isi == 0:
            print("Tidak ditemukan")

print(dfs(graf,'JakartaKota','Bekasi'))
