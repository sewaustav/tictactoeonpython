import pygame  
import sys
import random
import time

def bot(mas, ddigit):
    count_bot = ddigit / 2    
    if count_bot == 0:
        mas[1][1] = "x"
        return mas
    if count_bot == 1:
        rand = random.randint(1, 4)
        print(rand)
        if rand == 1:
            if mas[0][0] == 0 and mas[2][2] == 0 and mas[0][1] == 0 and mas[1][0] == 0:
                mas[0][0] = "x"
                return mas
            elif mas[0][1] == "o": 
                rand = 2 
                print(rand)
            elif mas[1][0] == "o":
                rand = 3
                print(rand) 
            else: 
                rand += 1
                print(rand)     
        if rand == 2:
            if mas[2][0] == 0 and mas[0][2] == 0 and mas[1][0] == 0 and mas[2][1] == 0:
                mas[2][0] = "x"
                return mas
            elif mas[1][0] == "o": 
                rand = 3
                print(rand)
            elif mas[2][1] == "o":
                rand = 3
                print(rand) 
            else: 
                rand += 1
                print(rand)       
        if rand == 3:
            if mas[0][2] == 0 and mas[2][0] == 0 and mas[0][1] == 0 and mas[1][2] == 0:
                mas[0][2] = "x"
                return mas
            elif mas[0][1] == "o":
                rand = 4
                print(rand) 
            elif mas[1][2] == "o":
                mas[0][0] = "x"
                return mas  
            else:
                rand += 1
                print(rand)          
        if rand == 4:
            if mas[2][2] == 0 and mas[0][0] == 0 and mas[1][2] == 0 and mas[2][1] == 0:
                mas[2][2] = "x"
                return mas
            elif mas[1][2] == "o":
                mas[0][0] = "x"
                return mas    
            elif mas[2][1] == "o":
                mas[0][0] = "x"
                return mas
            elif mas[2][2] != 0:
                mas[0][0] = "x"
                return mas 
            elif mas[0][0] != 0:
                mas[2][2] = "x"
                return mas            
    M = []            
    if count_bot == 2:
        for cur in range(3):
            for curr in range(3):
                if mas[cur][curr] == "o":
                    M.append(cur)
                    M.append(curr) 
        print(*M)                      
        if M[0] == M[2]:
            if M[1] == M[3] - 2 or M[1] == M[3] - 1:
                print("E")
                digit = M[0]
                count_o_e = 0
                for current in range(3):
                    if mas[digit][current] == "o":
                        count_o_e += 1
                        print(count_o_e)
                    elif mas[digit][current] == 0: 
                        mas[digit][current] = "x"
                        print("NNNNN")
                        return mas        
                if count_o_e == 2:
                    print("WWW")
                    if mas[0][0] == 0 and mas[2][2] == "x":
                        mas[0][0] = "x"
                        return mas
                    elif mas[2][2] == 0 and mas[0][0] == "x":
                        mas[2][2] = "x"
                        return mas
                    elif mas[0][2] == 0 and mas[2][0] == "x":
                        mas[0][2] = "x"
                        return mas
                    elif mas[2][0] == 0 and mas[0][2] == "x":
                        mas[2][0] = "x"
                        return mas   
                    elif mas[0][0] == 0 and mas[0][2] == "x":
                        mas[0][0] = "x"
                        return mas 
                    elif mas[2][2] == 0 and mas[0][2] == "x":
                        mas[2][2] = "x"
                        return mas 
                    elif mas[0][2] == 0 and mas[0][0] == "x":
                        mas[0][2] = "x"
                        return mas
                    elif mas[2][0] == 0 and mas[0][0] == "x":
                        mas[2][0] = "x"
                        return mas 
                    elif mas[0][0] == 0 and mas[2][0] == "x":
                        mas[0][0] = "x"
                        return mas
                    elif mas[2][2] == 0 and mas[2][0] == "x":
                        mas[2][2] = "x"
                        return mas
                    elif mas[0][2] == 0 and mas[2][2] == "x":
                        mas[0][2] = "x"
                        return mas 
                    elif mas[2][0] == 0 and mas[2][2] == "x":
                        mas[2][0] = "x"
                        return mas                            
            else:  
                print("Q") 
                if mas[0][0] == 0 and mas[2][2] == "x":
                    mas[0][0] = "x"
                    return mas
                elif mas[2][2] == 0 and mas[0][0] == "x":
                    mas[2][2] = "x"
                    return mas
                elif mas[0][2] == 0 and mas[2][0] == "x":
                    mas[0][2] = "x"
                    return mas
                elif mas[2][0] == 0 and mas[0][2] == "x":
                    mas[2][0] = "x"
                    return mas   
                elif mas[0][0] == 0 and mas[0][2] == "x":
                    mas[0][0] = "x"
                    return mas 
                elif mas[2][2] == 0 and mas[0][2] == "x":
                    mas[2][2] = "x"
                    return mas 
                elif mas[0][2] == 0 and mas[0][0] == "x":
                    mas[0][2] = "x"
                    return mas
                elif mas[2][0] == 0 and mas[0][0] == "x":
                    mas[2][0] = "x"
                    return mas 
                elif mas[0][0] == 0 and mas[2][0] == "x":
                    mas[0][0] = "x"
                    return mas
                elif mas[2][2] == 0 and mas[2][0] == "x":
                    mas[2][2] = "x"
                    return mas
                elif mas[0][2] == 0 and mas[2][2] == "x":
                    mas[0][2] = "x"
                    return mas 
                elif mas[2][0] == 0 and mas[2][2] == "x":
                    mas[2][0] = "x"
                    return mas         
        elif M[1] == M[3]:
            if M[0] == M[2] - 1 or M[0] == M[2] - 2:
                print("J")
                count_o_j = 0 
                digit = M[1]
                for current in range(3):
                    if mas[current][digit] == "o":
                        count_o_j += 1
                    elif mas[current][digit] == 0: 
                        mas[current][digit] = "x"   
                        return mas
                if count_o_j == 2:
                    if mas[0][0] == 0 and mas[2][2] == "x":
                        mas[0][0] = "x"
                        return mas
                    elif mas[2][2] == 0 and mas[0][0] == "x":
                        mas[2][2] = "x"
                        return mas
                    elif mas[0][2] == 0 and mas[2][0] == "x":
                        mas[0][2] = "x"
                        return mas
                    elif mas[2][0] == 0 and mas[0][2] == "x":
                        mas[2][0] = "x"
                        return mas   
                    elif mas[0][0] == 0 and mas[0][2] == "x":
                        mas[0][0] = "x"
                        return mas 
                    elif mas[2][2] == 0 and mas[0][2] == "x":
                        mas[2][2] = "x"
                        return mas 
                    elif mas[0][2] == 0 and mas[0][0] == "x":
                        mas[0][2] = "x"
                        return mas
                    elif mas[2][0] == 0 and mas[0][0] == "x":
                        mas[2][0] = "x"
                        return mas 
                    elif mas[0][0] == 0 and mas[2][0] == "x":
                        mas[0][0] = "x"
                        return mas
                    elif mas[2][2] == 0 and mas[2][0] == "x":
                        mas[2][2] = "x"
                        return mas
                    elif mas[0][2] == 0 and mas[2][2] == "x":
                        mas[0][2] = "x"
                        return mas 
                    elif mas[2][0] == 0 and mas[2][2] == "x":
                        mas[2][0] = "x"
                        return mas         
            else: 
                print("T") 
                if mas[0][0] == 0 and mas[2][2] == "x":
                    mas[0][0] = "x"
                    return mas
                elif mas[2][2] == 0 and mas[0][0] == "x":
                    mas[2][2] = "x"
                    return mas
                elif mas[0][2] == 0 and mas[2][0] == "x":
                    mas[0][2] = "x"
                    return mas
                elif mas[2][0] == 0 and mas[0][2] == "x":
                    mas[2][0] = "x"
                    return mas   
                elif mas[0][0] == 0 and mas[0][2] == "x":
                    mas[0][0] = "x"
                    return mas 
                elif mas[2][2] == 0 and mas[0][2] == "x":
                    mas[2][2] = "x"
                    return mas 
                elif mas[0][2] == 0 and mas[0][0] == "x":
                    mas[0][2] = "x"
                    return mas
                elif mas[2][0] == 0 and mas[0][0] == "x":
                    mas[2][0] = "x"
                    return mas 
                elif mas[0][0] == 0 and mas[2][0] == "x":
                    mas[0][0] = "x"
                    return mas
                elif mas[2][2] == 0 and mas[2][0] == "x":
                    mas[2][2] = "x"
                    return mas
                elif mas[0][2] == 0 and mas[2][2] == "x":
                    mas[0][2] = "x"
                    return mas 
                elif mas[2][0] == 0 and mas[2][2] == "x":
                    mas[2][0] = "x"
                    return mas                  
        else: 
            print("R")                    
            if mas[0][0] == 0 and mas[2][2] == "x":
                mas[0][0] = "x"
                return mas
            elif mas[2][2] == 0 and mas[0][0] == "x":
                mas[2][2] = "x"
                return mas
            elif mas[0][2] == 0 and mas[2][0] == "x":
                mas[0][2] = "x"
                return mas
            elif mas[2][0] == 0 and mas[0][2] == "x":
                mas[2][0] = "x"
                return mas   
            elif mas[0][0] == 0 and mas[0][2] == "x":
                mas[0][0] = "x"
                return mas 
            elif mas[2][2] == 0 and mas[0][2] == "x":
                mas[2][2] = "x"
                return mas 
            elif mas[0][2] == 0 and mas[0][0] == "x":
                mas[0][2] = "x"
                return mas
            elif mas[2][0] == 0 and mas[0][0] == "x":
                mas[2][0] = "x"
                return mas 
            elif mas[0][0] == 0 and mas[2][0] == "x":
                mas[0][0] = "x"
                return mas
            elif mas[2][2] == 0 and mas[2][0] == "x":
                mas[2][2] = "x"
                return mas
            elif mas[0][2] == 0 and mas[2][2] == "x":
                mas[0][2] = "x"
                return mas 
            elif mas[2][0] == 0 and mas[2][2] == "x":
                mas[2][0] = "x"
                return mas
    A = []  
    bo = False          
    if count_bot == 3:
        for dig in range(3):
            for di in range(3):
                if mas[dig][di] == "x":
                    A.append(dig)
                    A.append(di)
        print(*A)            
        if A[0] == A[2] or A[2] == A[4]:
            massive = A[2]
            for digi in range(3):
                if mas[massive][digi] == 0:
                    mas[massive][digi] = "x"
                    return mas 
                    bo = True                       
        if A[0] == A[4]:
            massive = A[0]
            for digi in range(3):
                if mas[massive][digi] == 0:  
                    mas[massive][digi] = "x"
                    return mas  
                    bo = True
        if A[1] == A[3] or A[1] == A[5]:
            co = A[1]
            for coc in range(3):
                if mas[coc][co] == 0:
                    mas[coc][co] = "x"
                    return mas
                    bo = True
        if A[3] == A[5]:
            co = A[3]
            for coc in range(3):
                if mas[coc][co] == 0:
                    mas[coc][co] = "x"
                    return mas
                    bo = True
        if mas[0][0] == "x" and mas[2][2] == 0:
            mas[2][2] = "x"
            return mas
            bo = True
        elif mas[2][2] == "x" and mas[0][0] == 0:
            mas[0][0] = "x"
            return mas
            bo = True
        elif mas[0][2] == "x" and mas[2][0] == 0:
            mas[2][0] = "x"
            return mas
            bo = True
        elif mas[2][0] == "x" and mas[0][2] == 0:
            mas[0][2] = "x"
            return mas
            bo = True
        if not bo:
            ra = random.randint(1, 3)
            print(ra)
            while ra > 0:
                for w in range(3):
                    for ww in range(3):
                        if mas[w][ww] == 0:
                            ra = ra - 1
                            if ra == 0:
                                mas[w][ww] = "x"
                                return mas 
    if count_bot == 4:
        for u in range(3):
            for e in range(3):
                if mas[u][e] == 0:
                    mas[u][e] = "x"
                    return mas   

def bot_2(mas, ddigit):
    count_bot_2 = ddigit // 2
    if count_bot_2 == 0:
        if mas[1][1] == "x":
            rand_2 = random.randint(1, 4)
            if rand_2 == 1:
                mas[0][0] = "o"
                return mas 
            elif rand_2 == 2:
                mas[0][2] = "o"
                return mas 
            elif rand_2 == 3:
                mas[2][2] = "o"
                return mas
            elif rand_2 == 4:
                mas[2][0] = "o"
                return mas
        elif mas[0][0] == "x" or mas[0][2] == "x" or mas[2][2] == "x" or mas[2][0] == "x":
            mas[1][1] = "o"
            return mas
        elif mas[0][1] == "x" or mas[1][0] == "x" or mas[1][2] == "x" or mas[2][1] == "x":
            mas[1][1] = "o"
            return mas
    W = []      
    sss = False           
    if count_bot_2 == 1:
        if mas[1][1] == "o":
            if mas[0][0] == "x" and mas[2][2] == "x":
                mas[1][0] = "o"
                return mas
            elif mas[2][0] == "x" and mas[0][2] == "x":
                mas[1][2] = "o"
                return mas    
        for ii in range(3):
            for jj in range(3):
                if mas[ii][jj] == "x":
                    W.append(ii)
                    W.append(jj)
        if W[0] == W[1] or W[2] == W[3]:
            print("W") 
            if mas[0][0] == "o" and mas[1][1] == "x" and mas[2][2] == "x":
                print("roo")
                r_o_o = random.randint(1, 2)
                if r_o_o == 1:
                    mas[2][0] = "o"
                    return mas 
                elif r_o_o == 2:
                    mas[0][2] = "o"
                    return mas    
            if mas[0][2] == "o" and mas[1][1] == "x" and mas[2][0] == "x":
                r_o_t = random.randint(1, 2)
                print("rot")
                if r_o_t == 1:
                    mas[0][0] = "o"
                    return mas 
                elif r_o_t == 2:
                    mas[2][2] = "o"
                    return mas 
            if mas[2][2] == "o" and mas[1][1] == "x" and mas[0][0] == "x":
                print("rtt")
                r_t_t = random.randint(1, 2)
                if r_t_t == 1:
                    mas[0][2] = "o"
                    return mas 
                elif r_t_t == 2:
                    mas[2][0] = "o"
                    return mas
            if mas[2][0] == "o" and mas[1][1] == "x" and mas[0][2] == "x":
                print("rto")
                r_t_o = random.randint(1, 2)
                if r_t_o == 1:
                    mas[0][0] = "o"
                    return mas
                elif r_t_o == 2:
                    mas[2][2] = "o"
                    return mas           
        print(*W)            
        if W[0] == W[2]:
            if W[1] == W[3] - 1 or W[1] == W[3] - 2:
                sss = True
                digit_2 = W[0]
                count_o_e_2 = 0
                for current_2 in range(3):
                    if mas[digit_2][current_2] == "x":
                        count_o_e_2 += 1
                        print(count_o_e_2)
                    elif mas[digit_2][current_2] == 0: 
                        mas[digit_2][current_2] = "o"
                        print("NNNNN")
                        return mas    
        if mas[0][0] == "x" and mas[1][1] == "x":
            sss = True
            mas[2][2] = "o"
            return mas 
        elif mas[2][2] == "x" and mas[1][1] == "x":
            sss = True
            mas[0][0] = "o"
            return mas
        elif mas[0][2] == "x" and mas[1][1] == "x":
            sss = True
            mas[2][0] = "o"
            return mas
        elif mas[2][0] == "x" and mas[1][1] == "x":
            sss = True
            mas[0][2] = "o"
            return mas 
        if W[1] == W[3]:
            if W[0] == W[2] - 1 or W[0] == W[2] - 2:
                sss = True
                digit_3 = W[1]
                count_o_e_3 = 0
                for current_3 in range(3):
                    if mas[current_3][digit_3] == "x":
                        count_o_e_3 += 1   
                        print(count_o_e_3)
                    elif mas[current_3][digit_3] == 0:
                        mas[current_3][digit_3] = "o"
                        return mas  
        if mas[1][1] == "o": 
            print("sss")
            if not sss:
                sec_step = random.randint(1, 4)      
                if sec_step == 1:
                    if mas[0][0] == 0:
                        mas[0][0] = "o"
                        return mas
                    else: sec_step += 1
                if sec_step == 2:
                    if mas[0][2] == 0:
                        mas[0][2] = "o"
                        return mas 
                    else: sec_step += 1
                if sec_step == 3:
                    if mas[2][2] == 0:
                        mas[2][2] = "o"
                        return mas
                    else: sec_step += 1
                if sec_step == 4:
                    if mas[2][0] == 0:
                        mas[2][0] = "o"
                        return mas
                    else: sec_step += 1
                if sec_step == 5:
                    r = random.randint(1, 2)
                    if r == 1:
                        mas[0][0] = "o"
                        return mas 
                    elif r == 2:
                        mas[2][2] = "o"
                        return mas 
                                     
    Z = []  
    Z_Z = [] 
    count_z_b = 0 
    count_z_a = 0            
    if count_bot_2 == 2:
        z_z = True
        if z_z:
            for t in range(3):
                for p in range(3):
                    if mas[t][p] == "o":
                        Z_Z.append(t)
                        Z_Z.append(p) 
                print(*Z_Z)        
               
            if Z_Z[0] == Z_Z[2]:
                z__z = Z_Z[0]
                
                for ai in range(3):
                    if mas[z__z][ai] == 0:
                        mas[z__z][ai] = "o"
                        count_z_a += 1
                        return mas         
            elif Z_Z[1] == Z_Z[3]:
                z___z = Z_Z[1]
                
                for bi in range(3):
                    if mas[bi][z___z] == 0:
                        mas[bi][z___z] = "o"
                        count_z_b += 1
                        return mas
        if count_z_a == 0 and count_z_b == 0:
            z_z = False                
        if mas[1][1] == "o":
            if mas[0][0] == "o" and mas[2][2] == 0:
                mas[2][2] = "o"
                return mas
            elif mas[2][2] == "o" and mas[0][0] == 0:
                mas[0][0] = "o" 
                return mas     
            elif mas[0][2] == "o" and mas[2][0] == 0:
                mas[2][0] = "o" 
                return mas
            elif mas[2][0] == "o" and mas[0][2] == 0:
                mas[0][2] = "o"
                return mas                                      
        print(z_z) 
        z_z_t = True       
        if not z_z:
            for c in range(3):
                for d in range(3):
                    if mas[c][d] == "x":
                        Z.append(c)
                        Z.append(d)
            print(*Z)
            if Z[0] == Z[2] or Z[2] == Z[4]:
                z = Z[2]
                for zz in range(3):
                    if mas[z][zz] == 0:
                        mas[z][zz] = "o"
                        z_z_t = False
                        return mas
            if Z[0] == Z[4]:
                zzz = Z[0]
                for zzzz in range(3):
                   if mas[zzz][zzzz] == 0:
                       mas[zzz][zzzz] = "o"
                       z_z_t = False
                       return mas
            if Z[1] == Z[3] or Z[1] == Z[5]:
                h = Z[1]
                for hh in range(3):
                    if mas[hh][h] == 0:
                        mas[hh][h] = "o"
                        z_z_t = False
                        return mas
            if Z[3] == Z[5]:
                hhh = Z[3]
                for hhhh in range(3):
                    if mas[hhhh][hhh] == 0:
                        mas[hhhh][hhh] = "o"
                        z_z_t = False
                        return mas
            print(z_z_t, "1")
            z_z_t_t = z_z_t

            print(z_z_t_t)
            if z_z_t_t:
                print("p")
                if mas[0][0] == "o":
                    if mas[0][1] == 0 and mas[0][2] == 0:
                        mas[0][2] = "o"
                        return mas
                    elif mas[1][0] == 0 and mas[2][0] == 0:
                        mas[2][0] = "o"
                        return mas
                if mas[2][2] == "o":
                    if mas[1][2] == 0 and mas[0][2] == 0:
                        mas[0][2] = "o"
                        return mas
                    elif mas[2][1] == 0 and mas[2][0] == 0:
                        mas[2][0] = "o"
                        return mas
                if mas[2][0] == "o":
                    if mas[1][0] == 0 and mas[0][0] == 0:
                        mas[0][0] = "o"
                        return mas
                    elif mas[2][1] == 0 and mas[2][2] == 0:
                        mas[2][2] = "o"
                        return mas
                if mas[0][2] == "o":
                    if mas[0][1] == 0 and mas[0][0] == 0:
                        mas[0][0] = "o"
                        return mas
                    elif mas[1][2] == 0 and mas[2][2] == 0:
                        mas[2][2] = "o"
                        return mas    


            if mas[1][1] == "x" and mas[0][0] == "x":
                mas[2][2] = "o"
                z_z_t_t = False
                return mas
            elif mas[1][1] == "x" and mas[2][2] == "x":
                mas[0][0] = "o"
                z_z_t_t = False
                return mas
            elif mas[1][1] == "x" and mas[0][2] == "x":
                mas[2][0] = "o"
                z_z_t_t =False
                return mas
            elif mas[1][1] == "x" and mas[2][0] == "x":
                mas[0][2] = "o"
                z_z_t_t = False
                return mas
    
    J = []
    if count_bot_2 == 3:
        if mas[1][1] == "o":
            if mas[0][0] == 0 and mas[2][2] == "o":
                mas[0][0] = "o"
                return mas  
            elif mas[2][2] == 0 and mas[0][0] == "o":
                mas[2][2] = "o"
                return mas 
            elif mas[0][2] == 0 and mas[2][0] == "o":
                mas[0][2] = "o"
                return mas                  
            elif mas[2][0] == 0 and mas[0][2] == "o":
                mas[2][0] = "o"
                return mas  
                                                                   
        
        if mas[0][0] == "x" and mas[1][0] == "x" and mas[2][0] == 0:
            mas[2][0] = "o"
            return mas  
        elif mas[0][0] == "x" and mas[2][0] == "x" and mas[1][0] == 0:
            mas[1][0] = "o"
            return mas
        elif mas[1][0] == "x" and mas[2][0] == "x" and mas[0][0] == 0:
            mas[0][0] = "o"
            return mas                                         
        
        elif mas[0][1] == "x" and mas[1][1] == "x" and mas[2][1] == 0:
            mas[2][1] = "o"
            return mas  
        elif mas[0][1] == "x" and mas[2][1] == "x" and mas[1][1] == 0:
            mas[1][1] = "o"
            return mas
        elif mas[1][1] == "x" and mas[2][1] == "x" and mas[0][1] == 0:
            mas[0][1] = "o"
            return mas

        elif mas[0][2] == "x" and mas[1][2] == "x" and mas[2][2] == 0:
            mas[2][2] = "o"
            return mas  
        elif mas[0][2] == "x" and mas[2][2] == "x" and mas[1][2] == 0:
            mas[1][2] = "o"
            return mas
        elif mas[1][2] == "x" and mas[2][2] == "x" and mas[0][2] == 0:
            mas[0][2] = "o"
            return mas 

        elif mas[0][0] == "x" and mas[0][1] == "x" and mas[0][2] == 0:
            mas[0][2] = "o"
            return mas  
        elif mas[0][0] == "x" and mas[0][2] == "x" and mas[0][1] == 0:
            mas[0][1] = "o"
            return mas
        elif mas[0][1] == "x" and mas[0][2] == "x" and mas[0][0] == 0:
            mas[0][0] = "o"
            return mas       
        
        elif mas[1][0] == "x" and mas[1][1] == "x" and mas[1][2] == 0:
            mas[1][2] = "o"
            return mas  
        elif mas[1][0] == "x" and mas[1][2] == "x" and mas[1][1] == 0:
            mas[1][1] = "o"
            return mas
        elif mas[1][1] == "x" and mas[1][2] == "x" and mas[1][0] == 0:
            mas[1][0] = "o"
            return mas

        elif mas[2][0] == "x" and mas[2][1] == "x" and mas[2][2] == 0:
            mas[2][2] = "o"
            return mas  
        elif mas[2][0] == "x" and mas[2][2] == "x" and mas[2][1] == 0:
            mas[2][1] = "o"
            return mas
        elif mas[2][1] == "x" and mas[2][2] == "x" and mas[2][0] == 0:
            mas[2][0] = "o"
            return mas  

        elif mas[0][0] == "x" and mas[1][1] == "x" and mas[2][2] == 0:
            mas[2][2] = "o"
            return mas
        elif mas[2][2] == "x" and mas[1][1] == "x" and mas[0][0] == 0:
            mas[0][0] = "o"
            return mas
        elif mas[0][0] == "x" and mas[2][2] == "x" and mas[1][1] == 0:
            mas[1][1] = "o"
            return mas

        elif mas[0][2] == "x" and mas[1][1] == "x" and mas[2][0] == 0:
            mas[2][0] = "o"
            return mas
        elif mas[2][0] == "x" and mas[1][1] == "x" and mas[0][2] == 0:
            mas[0][2] = "o"
            return mas
        elif mas[0][2] == "x" and mas[2][0] == "x" and mas[1][1] == 0:
            mas[1][1] = "o"
            return mas                        

        else:
            for mi in range(3):
                for ni in range(3):
                    if mas[mi][ni] == 0:
                        mas[mi][ni] = "o"
                        return mas
                        break

            






            

                            
                        








                                 
def check_win(mas, sign):
    for m in mas:
        if m.count(sign) == 3:
            return sign
    for n in range(3):
        if mas[0][n] == sign and mas[1][n] == sign and mas[2][n] == sign: 
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign: 
        return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign: 
        return sign
    count_zero = 0    
    for l in range(3):
        for v in range(3):
            if mas[l][v] == 0:
                count_zero += 1
    if count_zero == 0:
        return "draw"            
    return False                    

pygame.init()

size = 100  
margin = 15 
width = heigth = size * 3 + margin * 4 
size_window = (width, heigth) 

screen = pygame.display.set_mode(size_window) 
pygame.display.set_caption("Tic Tac Toe") 

BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 
BLUE = (0, 0, 255) 
RED = (255, 0, 0) 

 
game_over = False

field = [[0] * 10 for gen in range(3)] 

game = True
hello = True
player_x = False
player_y = False
player_2 = False
game_1 = False
continue_game = False
q = 1
q_x = False
q_o = False
w = False

player = 10000

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0) 
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_g:
            continue_game = True    
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            continue_game = False   
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            if q % 2 != 0:
                q_o = True
                game_1 = True
                player = 0
                player_x = False
                player_y = True
                continue_game = True
                q += 1
            elif q % 2 == 0:
                q_x = True
                game_1 = True
                player = 1
                field[1][1] = "x"
                player_y = False
                player_x = True
                continue_game = True  
                q += 1  
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            q = 0
            q_x = False
            q_o = False
            continue_game = False        
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s and not game_1:
            player = 0
            player_2 = True
            game_1 = True
        elif event.type == pygame.KEYDOWN and not game_1 and event.key == pygame.K_x:
            player = 1
            player_x = True
            field[1][1] = "x"
            game_1 = True
        elif event.type == pygame.KEYDOWN and not game_1 and event.key == pygame.K_o:
            player = 0
            player_y = True
            game_1 = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DELETE:
            game = False    
        elif event.type == pygame.KEYDOWN and not game_over and event.key == pygame.K_SPACE and game_1:
            if player_x:    
                if player % 2 == 0:
                    bot(field, player)
                    player += 1
            elif player_y:
                if player % 2 != 0:
                    bot_2(field, player)
                    player += 1    
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over and game_1: 
            x_mouse, y_mouse = pygame.mouse.get_pos() 
            print("x = ", x_mouse, "y = ", y_mouse)
            row = y_mouse // (margin + size) 
            column = x_mouse // (margin + size)
            if field[row][column] == 0:
                if player_x: 
                    if player % 2 != 0: 
                        field[row][column] = "o"  
                    player += 1 
                elif player_y:
                    if player % 2 == 0:
                        field[row][column] = "x"
                    player += 1
                elif player_2:
                    if player % 2 == 0:
                        field[row][column] = "x"
                        player += 1
                    else:
                        field[row][column] = "o"
                        player += 1                       
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and game_1:
            if not continue_game:
                game_over = False 
                field = [[0] * 10 for gen in range(3)]
                player = 0
                game_1 = False
                player_x = False
                player_y = False
                player_2 = False
                screen.fill(BLACK)
            if continue_game:
                if q_o:
                    game_over = False
                    field = [[0] * 3 for ij in range(3)]
                    field[1][1] = "x"
                    player = 1
                    screen.fill(BLACK)
                if q_x:
                    game_over = False
                    field = [[0] * 3 for ijj in range(3)]
                    player = 0
                    screen.fill(BLACK)
                else:    
                    if player_x:
                        game_over = False
                        field = [[0] * 3 for ij in range(3)]
                        field[1][1] = "x"
                        player = 1
                        screen.fill(BLACK)  
                    elif player_y:
                        game_over = False
                        field = [[0] * 3 for ijj in range(3)]
                        player = 0
                        screen.fill(BLACK)
                    elif player_2:
                        game_over = False
                        field = [[0] * 3 for iij in range(3)]
                        player = 0
                        screen.fill(BLACK)              

        
    if not game_over:        
        for i in range(3):
            for j in range(3):
                if field[i][j] == "x":  
                    color = RED
                elif field[i][j] == "o": 
                    color = BLUE    
                else: color = WHITE         
                x = j * size + margin * (j + 1) 
                y = i * size + margin * (i + 1) 
                pygame.draw.rect(screen, color, (x, y, size, size)) 
                if color == RED:
                    pygame.draw.line(screen, WHITE, (x + 5, y + 5), (x + size - 5, y + size - 5), 4)
                    pygame.draw.line(screen, WHITE, (x + size - 5, y + 5), (x + 5, y + size -5), 4)
                elif color == BLUE: 
                    pygame.draw.circle(screen, WHITE, (x + size // 2, y + size // 2), size // 2 - 3, 4)

        if (player - 1) % 2 == 0:
            game_over = check_win(field, "x")
        else: game_over = check_win(field, "o")


        if game_over:
            time.sleep(0.5)
            screen.fill(BLACK)
            if game_over != "draw":
                font = pygame.font.SysFont('verdana', 80) 
                text1 = font.render(game_over, True, WHITE)
                text_rect = text1.get_rect()
                text_x = (3 * size + margin) // 2  
                text_y = (2 * size + margin * 2) // 2 
                screen.blit(text1, (text_x, text_y)) 
            elif game_over == "draw":
                font = pygame.font.SysFont('verdana', 80) 
                text2 = font.render(game_over, True, WHITE)
                text_rect = text2.get_rect()
                text_x = (3 * size + margin) // 4
                text_y = (2 * size + margin * 2) // 2
                screen.blit(text2, (text_x, text_y))   
            
                

    pygame.display.update()        