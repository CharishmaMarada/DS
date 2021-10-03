from itertools import permutations

def calculate_psi(msg,bs):
  nsl=[]
  tl={}
  for i in range(0,len(msg),bs):
    temp = msg[i:i+bs]
    nsl.append(temp)        
  for j,z in enumerate(nsl):
    counter=1
    for k in range(j+1,len(nsl)):
     if z == nsl[k]:
       counter +=1
    tl[z]=counter
    count=0
    n=tl.__len__()
    for x,y in tl.items():
        count=count+float((y/n)**2)
  return count

with open('alice_permuted.txt', 'r') as initial_input:
    decipher_text = initial_input.read().replace('\n','')
initial_input.close()
bs=3
perm_size = 7
perm_list = list(permutations(range(0, perm_size)))
text = [decipher_text[i: i + perm_size] for i in range(0, len(decipher_text), perm_size)]
for p in perm_list:
    msg = ""
    for t in text:
        for x in p:
            if len(t) == perm_size:
                msg += t[x]
            else:
                msg += t
    psi=calculate_psi(msg,bs)
    print("permutation is: %s and its psi value is %s and its corresponding first 25 characters of text is  %s"%(p,psi,msg[:25]))


