#import numpy as np
#import numpy.ma as ma

               #  N   M     V     E
#t           = [[0.75,0.25,   0,   0],   #S
#              [0.11,0.33,0.11,0.44],    #N
#              [0.25,0   ,0.75,   0],    #M
#              [1   ,   0,   0,   0]]    #V


              # N   M V
#e          = [[0.44,0,0],   #mary
#              [0.22,0,0],   #jane
#              [0.11,0.75,0], # will
#              [0.22,0,0.25],    #spot
#              [0,0.25,0],   #can
#              [0,0,0.5],    #see
#              [0,0,0.25]]   #pat
                  #  N   A     V     E
t           = [[0,0.5,   0.5,   0],   #S
              [0 ,0  ,0     ,   1],    #N
              [0.5,  0.25,0.25,   0],    #A
              [0   ,   1,   0,   0]]    #V


              # N   A V
e          = [[0,0.5,0],   #this #word1 #Dieses Wort kommt N vor 
              [0,0,1],   #is #word2 # Dieser Wort kommt als N vor
              [0,0.5,0], #a #word3 #Dieses Wort kommt als N und M vor
              [1,0,0]]    #demo #word4 #Dieses Wort kommt als N und V vor 
              
              
#prev_states = ["S" , "N" , "M" , "V", "E"]


#sentence="this is a demo"
#sentence="demo demo demo demo"
#sentence="this this this this"
#sentence="is this a demo"
#sentence="is this is this"
sentence="a demo is this"           
sentence="a demo a demo"              
#prev_states = ["S" , "N" , "M" , "V", "E"]


res=0

cur_state = [[1,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0]]
             
             
             
val_state = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]



#val_state2 = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
            
                         
n = []

m  =[]

v = []

             
state_mat = [[1,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0]]
      

tokens = sentence.split()
print(tokens)


sentence_encoded = []
       
for word in tokens:
    
    if(word == "this"):
       sentence_encoded.append(0)
    elif(word== "is"):
       sentence_encoded.append(1)   
    elif(word== "a"):
       sentence_encoded.append(2)
    elif(word== "demo"):
       sentence_encoded.append(3)




#print(sentence_encoded)
j = 0 
i = 0
k=0
while(cur_state[2][5]  != 1):

 if(cur_state[0][0]==1 and state_mat[0][0]==1):
      
      #S
     x = sentence_encoded[0]
      
     n = t[0][0] * e[x][0]    
     m = t[0][1] * e[x][1]
     v = t[0][2] * e[x][2]
      
     if(n > 0):
        
       val_state[0][1] = n
       #val_state2[0][0][1]=n
       cur_state[0][1] = 1
       state_mat[0][1]= 1
       i=0
       #k=i
       j=1
     if(m > 0):
        
       val_state[1][1] = m
       #val_state2[0][1][1]=n
       cur_state[1][1] = 1
       state_mat[1][1]= 1
       i=1
       #k=i
       j=1
     if(v > 0):
       val_state[2][1] = v
       #val_state2[0][2][1]=n
       cur_state[2][1] = 1 
       state_mat[2][1]= 1
       i=2
       #k=i
       j=1
     if(cur_state[0][1]==1 or cur_state[1][1]== 1 or cur_state[2][1] == 1):
       state_mat[0][1] = cur_state[0][1]
       state_mat[1][1] = cur_state[1][1]
       state_mat[2][1] = cur_state[2][1] 
     else:
       break
     state_mat[0][0] = 0
      
      
      
      #print(val_state)
      #print(cur_state
      
      
      

      #and state_mat[i][j] ==1)
      
      
      

 if(cur_state[0][1]==1 and state_mat[0][1] == 1):
    
    
    #N
    x = sentence_encoded[1]
             
    
    n = val_state[0][1]*t[1][0] * e[x][0]
    m = val_state[0][1]*t[1][1] * e[x][1]
    v = val_state[0][1]*t[1][2] * e[x][2]
    
    
    
    
    #print(n,m,v)
    
    if(n > 0):
        
       val_state[0][2] = n
       state_mat[0][2]= 1
       cur_state[0][2] = 1
    if(m > 0):
        
       val_state[1][2] = m
       cur_state[1][2] = 1
       state_mat[1][2]= 1
    if(v > 0):
        
        
       val_state[2][2] = v
       cur_state[2][2] = 1 
       state_mat[2][2]= 1
    if(cur_state[0][2]==1 or cur_state[1][2]== 1 or cur_state[2][2] == 1):
       state_mat[0][2] = cur_state[0][2]
       state_mat[1][2] = cur_state[1][2]
       state_mat[2][2] = cur_state[2][2] 
    else:
       break
      
    #print(val_state)
    
    #print(cur_state)
    state_mat[0][1] = 0 
    
    #print("")
 if(cur_state[1][1]==1 and state_mat[1][1] == 1):
 
    #M    

    x = sentence_encoded[1]
     

    
    n = val_state[1][1]*t[2][0] * e[x][0]    
    m = val_state[1][1]*t[2][1] * e[x][1]
    v = val_state[1][1]*t[2][2] * e[x][2]
    #print(n,m,v)
    
    if(n > 0):
        
       val_state[0][2] = n
       state_mat[0][2] = 1
       cur_state[0][2] = 1
    if(m > 0):
       val_state[1][2] = m
       cur_state[1][2] = 1
       state_mat[1][2] = 1
    if(v > 0):
        
       val_state[2][2] = v
       cur_state[2][2] = 1 
       state_mat[2][2] = 1
    if(cur_state[0][2]==1 or cur_state[1][2]== 1 or cur_state[2][2] == 1):
       state_mat[0][2] = cur_state[0][2]
       state_mat[1][2] = cur_state[1][2]
       state_mat[2][2] = cur_state[2][2] 
    else:
      break
    #print(val_state)
    #print(cur_state)
    
    state_mat[1][1] = 0
    #print("")

   

    #print("")

 if(cur_state[2][1]==1 and state_mat[2][1]==1):
       
    #V
    x = sentence_encoded[1]  
    
    #val_state2[2][0][2] = val_state2[0][0][1]*t[1][2]*e[x][2]
    #val_state2[2][1][2] = val_state2[0][1][1]*t[2][2]*e[x][2]
    #val_state2[2][2][2] = val_state2[0][2][1]*t[3][2]*e[x][2]

    n = val_state[2][1]*t[3][0] * e[x][0]    
    m = val_state[2][1]*t[3][1] * e[x][1]
    v = val_state[2][1]*t[3][2] * e[x][2]
    
    print(n,m,v)
    if(n > 0):
       res             = n 
       val_state[0][2] = n
       state_mat[0][2] = 1
       cur_state[0][2] = 1
    if(m > 0):
       val_state[1][2] = m
       cur_state[1][2] = 1
       state_mat[1][2] = 1
    if(v > 0):
       val_state[2][2] = v
       cur_state[2][2] = 1 
       state_mat[2][2] = 1
    if(cur_state[0][2]==1 or cur_state[1][2]== 1 or cur_state[2][2] == 1):
       state_mat[0][2] = cur_state[0][2]
       state_mat[1][2] = cur_state[1][2]
       state_mat[2][2] = cur_state[2][2] 
    else:
      break
      
    #print(val_state)
    #print(cur_state)
    
    state_mat[2][1] = 0
    
    #print("")
    
    #print(val_state)
    #print(cur_state)
    
   
   
    #print("")   
 if(cur_state[0][2]==1 and state_mat[0][2] == 1):
    
    #N
    x = sentence_encoded[2]    
    
    
    n = val_state[0][2]*t[1][0] * e[x][0]    
    m = val_state[0][2]*t[1][1] * e[x][1]
    v = val_state[0][2]*t[1][2] * e[x][2]
    if(n > 0):
        
       val_state[0][3] = n
       state_mat[0][3]= 1
       cur_state[0][3] = 1
    if(m > 0):
        
       val_state[1][3] = m
       cur_state[1][3] = 1
       state_mat[1][3]= 1
    if(v > 0):
        
       val_state[2][3] = v
       cur_state[2][3] = 1 
       state_mat[2][3]= 1
    if(cur_state[0][3]==1 or cur_state[1][3]== 1 or cur_state[2][3] == 1):
       state_mat[0][3] = cur_state[0][3]
       state_mat[1][3] = cur_state[1][3]
       state_mat[2][3] = cur_state[2][3] 
    else:
       break
    
    #print(cur_state)
    state_mat[0][2] = 0 
    
    #print("")
    
 
 if(cur_state[1][2]==1 and state_mat[1][2] == 1):
    
    
    x = sentence_encoded[2] 

    #x = sentence_encoded[2]
     
      
    
    n = val_state[1][2]*t[2][0] * e[x][0]    
    m = val_state[1][2]*t[2][1] * e[x][1]
    v = val_state[1][2]*t[2][2] * e[x][2]
    
    #print(n,m,v)
    if(n > 0):
        
       val_state[0][3] = n
       state_mat[0][3] = 1
       cur_state[0][3] = 1
    if(m > 0):
        
       val_state[1][3] = m
       cur_state[1][3] = 1
       state_mat[1][3] = 1
    if(v > 0):
        
       val_state[2][3] = v
       cur_state[2][3] = 1 
       state_mat[2][3] = 1
    if(cur_state[0][3]==1 or cur_state[1][3]== 1 or cur_state[2][3] == 1):
       state_mat[0][3] = cur_state[0][3]
       state_mat[1][3] = cur_state[1][3]
       state_mat[2][3] = cur_state[2][3] 
    else:
      break
        
    state_mat[1][2] = 0
    
    #print("")
    
    #print(val_state)
    #print(cur_state)
    #print
 if(cur_state[2][2]==1 and state_mat[2][2]==1):
    
    x = sentence_encoded[2]
    
    
    n = val_state[2][2]*t[3][0] * e[x][0]    
    m = val_state[2][2]*t[3][1] * e[x][1]
    v = val_state[2][2]*t[3][2] * e[x][2]
    
    print(n,m,v)
    if(n > 0):
       res             = n 
       val_state[0][3] = n
       state_mat[0][3] = 1
       cur_state[0][3] = 1
    if(m > 0):
       val_state[1][3] = m
       cur_state[1][3] = 1
       state_mat[1][3] = 1
    if(v > 0):
       val_state[2][3] = v
       cur_state[2][3] = 1 
       state_mat[2][3] = 1
    if(cur_state[0][3]==1 or cur_state[1][3]== 1 or cur_state[2][3] == 1):
       state_mat[0][3] = cur_state[0][3]
       state_mat[1][3] = cur_state[1][3]
       state_mat[2][3] = cur_state[2][3] 
    else:
      break
    #print(val_state)
    #print(cur_state)
    
    state_mat[2][2] = 0
    
    #print("")
    
    #print(val_state)
    #print(cur_state)
    
   
   
   
    #print("")   
 if(cur_state[0][3]==1 and state_mat[0][3]==1):
    
    ##########################################################
    x = sentence_encoded[3] 
       
    
    n = val_state[0][3]*t[1][0] * e[x][0]    
    m = val_state[0][3]*t[1][1] * e[x][1]
    v = val_state[0][3]*t[1][2] * e[x][2]
    #print(n,m,v)
    if(n > 0):
       #res = n 
       val_state[0][4] = n
       state_mat[0][4] = 1
       cur_state[0][4] = 1
    if(m > 0):
        
       val_state[1][4] = m
       cur_state[1][4] = 1
       state_mat[1][4] = 1
    if(v > 0):
        
       val_state[2][4] = v
       cur_state[2][4] = 1 
       state_mat[2][4] = 1
    if(cur_state[0][4]==1 or cur_state[1][4]== 1 or cur_state[2][4] == 1):
       state_mat[0][4] = cur_state[0][4]
       state_mat[1][4] = cur_state[1][4]
       state_mat[2][4] = cur_state[2][4] 
    else:
      break
    #print(val_state)
    #print(cur_state)
    state_mat[0][3] = 0 
    
    #print("")
     
    #print("")
 if(cur_state[1][3]==1 and state_mat[1][3]==1):
    x = sentence_encoded[3]
    
       
    
    n = val_state[1][3]*t[2][0] * e[x][0]    
    m = val_state[1][3]*t[2][1] * e[x][1]
    v = val_state[1][3]*t[2][2] * e[x][2]
    
    #print(n,m,v)
    if(n > 0):
        
       val_state[0][4] = n
       state_mat[0][4] = 1
       cur_state[0][4] = 1
    if(m > 0):
        
       val_state[1][4] = m
       cur_state[1][4] = 1
       state_mat[1][4] = 1
    if(v > 0):
        
       val_state[2][4] = v
       cur_state[2][4] = 1 
       state_mat[2][4] = 1
    if(cur_state[0][4]==1 or cur_state[1][4]== 1 or cur_state[2][4] == 1):
       state_mat[0][4] = cur_state[0][4]
       state_mat[1][4] = cur_state[1][4]
       state_mat[2][4] = cur_state[2][4] 
    else:
      break
    state_mat[1][3] = 0
    
    #print("")
    
    #print(val_state)
    #print(cur_state)
    
   
   
   
    print("")

 if(cur_state[2][3]==1 and state_mat[2][3]==1):
    
    
    x = sentence_encoded[3]
   
       
    
    n = val_state[2][3]*t[3][0] * e[x][0]    
    m = val_state[2][3]*t[3][1] * e[x][1]
    v = val_state[2][3]*t[3][2] * e[x][2]
    
    #print(n,m,v)
    if(n > 0):
       res             = n 
       val_state[0][4] = n
       state_mat[0][4] = 1
       cur_state[0][4] = 1
    if(m > 0):
       val_state[1][4] = m
       cur_state[1][4] = 1
       state_mat[1][4] = 1
    if(v > 0):
       val_state[2][4] = v
       cur_state[2][4] = 1 
       state_mat[2][4] = 1
    if(cur_state[0][4]==1 or cur_state[1][4]== 1 or cur_state[2][4] == 1):
       state_mat[0][4] = cur_state[0][4]
       state_mat[1][4] = cur_state[1][4]
       state_mat[2][4] = cur_state[2][4] 
    else:
      break
      
    #print(val_state)
    #print(cur_state)
    
    state_mat[2][3] = 0
    
    #print("")
    
    #print(val_state)
    #print(cur_state)
    #print(state_mat)   
 if(cur_state[0][4]==1 and state_mat[0][4]==1):
 
 
    
    n = val_state[0][4]* t[1][3]    
    #print(n,m,v)
    
    
    
    
    if(n > 0):
       val_state[0][5] = n
       state_mat[0][5] = 1
       cur_state[2][5] = 1
       state_mat[2][5] = 1
       val_state[1][5] = res*t[1][3]
    else:
       break       
    #print(val_state[0][5])
    #print(val_state[1][5])
    #print(val_state)
    #print(cur_state)
    state_mat[0][4] = 0 
    
  
  
  
 #if(cur_state[1][0]==1):
 #  print("")
 
 
 
 if(cur_state[1][4]== 1 and state_mat[1][4] == 1):
    n = val_state[1][4]* t[1][3]    
    #m = val_state[0][3] * e[1][2]
    #v = val_state[0][3]* e[0][3]
    #print(n,m,v)
    if(n > 0):
       val_state[0][5] = n
       state_mat[0][5] = 1
       cur_state[2][5] = 1
       state_mat[2][5] = 1
       #val_state[1][5] = res*t[1][3]
    #else:
    #   break
    #if(m > 0):
    #   val_state[1][5] = m
    #   cur_state[1][5] = 1
    #   state_mat[1][5] = 1
    #if(v > 0):
    #   val_state[2][5] = v
    #   cur_state[2][5] = 1 
    #   state_mat[2][5] = 1
    #print(val_state[0][5])
    #print(val_state[1][5])
    #print(val_state)
    #print(cur_state)
    state_mat[1][4] = 0 
    #print(res*val_state[0][4])
    
  
  
  
 #if(cur_state[2][0]==1):
 #   print("")
 
 
 
   
 if(cur_state[2][4]==1 and state_mat[2][4] == 1):
    n = val_state[2][4]* t[1][3]    
    #m = val_state[0][3] * e[1][2]
    #v = val_state[0][3]* e[0][3]
    #print(n,m,v)
    if(n > 0):
       val_state[0][5] = n
       state_mat[0][5] = 1
       cur_state[2][5] = 1
       state_mat[2][5] = 1
       val_state[1][5] = res*t[1][3]
    #else:
    # break
    
    #if(m > 0):
    #   val_state[1][5] = m
    #   cur_state[1][5] = 1
    #   state_mat[1][5] = 1
    #if(v > 0):
    #   val_state[2][5] = v
    #   cur_state[2][5] = 1 
    #   state_mat[2][5] = 1
    #print(val_state[0][5])
    #print(val_state[1][5])
    #print(val_state)
    #print(cur_state)
    state_mat[2][4] = 0 
    #print(res*val_state[0][4])
     

for row in val_state:
   print(row)
   
for row in cur_state:
   print(row)   



#for row in val_state2:
#  for r in row:
#   print(r)
     
            
