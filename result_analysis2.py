
fh=open ("result.txt")
print (fh.read())
count=0
result_list=[]
while True:
     line=fh.readline()
     if line =="":
          break
     result_list.append ([])
     if len(line)>1: 
          
          x=line.split()
          if (count %2==0):
              
               x.pop (0)
               x.pop (0)
               x.pop (-1)
               name_list=[]
               n=""
           
               for i in x:
                    if (i.isdigit()):
                         break
                    n+=" "+i
                                   
                    
               name_list.append(n)
               
               while True:
                    for i in range (6):
                         if (x[i].isalpha()):
                              x.remove(x[i])
                    if (x[0].isdigit()):
                         break
               x.insert(0,n)
                    
               
              
          else:
               for i in x:
                    if not i.isdigit():
                         x.remove(i)
          for i in x:
               result_list[count].append(i)
          count+=1
for i in result_list:
     print (i)
