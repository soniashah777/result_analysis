import mysql.connector as my

con=my.connect(host="localhost",port="3308",user="root" ,database="resultdb",password="allen")

def subject_name(code):
     #sname,mathb, hindi, math,sci,sst,ca, english,fmm, ai
     if code == "241":
          return "mathb"
     elif code== "002":
          return "hindi"
     elif code== "041":
          return "math"
     elif code=="086":
          return "sci"
     elif code == "087":
          return "sst"
     elif code =="165":
          return "ca"
     elif code== "184":
          return "english"
     elif code == "405":
          return "fmm"
     elif code == "417":
          return "ai"

     else:
          print("invalid input")
          return None
     
fh=open ("result.txt")
count=0
result_list=[]
#pd=pd. dataFrame(cols=["gan","name","english","hindi","math","physics","chemistry","biology","cs","ped","ai","bst","account","economics"]) 

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
m1,m2,m3,m4,m5,m6,subject1,subject2,subject3,subject4,subject5,subject6=None,None,None,None,None,None,None,None,None,None,None,None
#for i in result_list:
#     print (i)
count=0
for i in result_list:
     if (len(i)>0):
          
          if (count%2==0):
               s_name=i[0]
               subject1=subject_name(i[-6])
               print (subject1)
               subject2=subject_name(i[-5])
               print (subject2)
               subject3=subject_name(i[-4])
               print (subject3)
               subject4=subject_name(i[-3])
               print (subject4)
               subject5=subject_name(i[-2])
               print (subject5)
               subject6=subject_name(i[-1])
               print (subject6)
          else:
               m1=i[0]
               print (i[0])
               m2=i[1]
               print (m2)
               m3=i[2]
               print (m3)
               m4=i[3]
               print (m4)
               m5=i[4]
               print (m5)
               m6=i[5]
               print (m6)
          
     
               mycursor=con.cursor()
               sql = "INSERT INTO xresult (sname, "+subject1+","+subject2+","+subject3+","+subject4+","+subject5+","+subject6+") VALUES ('"+s_name+"',"+str(m1)+", "+str(m2)+", "+str(m3)+", "+str(m4)+", "+str(m5)+","+ str(m6)+");"
               #val = (s_name,float(m1), float(m2),float(m3),float(m4),float(m5),float(m6))
               print (sql)
               mycursor.execute(sql)
               con.commit()

     count+=1
con.close()
