import csv
import binascii
predicates = []
tables=[]
final=""

def bitmaps(p,num,count):
   q=''.join(str(i) for i in p)
   str_num = str(num);
   ans=""
   if count%2 ==0:
       ans=ans+"0"+str_num+"00 0000 "
   else :
       ans=ans+"0"+str_num+" 0000 00"
   for i in range(125*num):
       qq =str(hex(int(q[i*8 : i*8 + 8],2)))
       if len(qq)==4:
           ans = ans + qq[2:]
       else:
           ans= ans+ '0'+qq[2:]
       count = count + 1
       if count%2==0:
           ans += " "
   return(ans,count) #working tested
counter_total=0
with open("test.csv", 'r') as f:
    data_raw = list(list(rec) for rec in csv.reader(f, delimiter='#'))
    for row in data_raw:
        tables.append(row[0].split(','))
        predicates.append(row[2].split(','))
        if int(row[3]) < 1:
            print("Queries must have non-zero cardinalities")
            exit(1)
f1 = 0 
for tab in tables:
    ppp=0
    siz1=len(tab)
    final_arr=[]
    for i in range(siz1*1000):
        final_arr.append(1)
    for k in range(int(siz1)):
        x2=tab[k]
        x3=x2.split(' ')
        # print(x3)
        prev_tables=x3[1]
        arr=[]
        for i in range(1000):
            arr.append(1)
        ro = predicates[f1]
        size = len(ro)
        size=size/3.0
        # print(size)
        for i in range(int(size)):
            title=ro[3*i]
            # print(title)
            x=title.split('.')
            table=x[0]
            pred=x[1]
            # print(pred)
            # print(table)
            sign=ro[3*i+1]
            # print(sign)
            value=ro[3*i+2]
            count=0
            # print(value)
            # print("done2")
            if table==prev_tables:
                # print(prev_tables)
                # print("inside")
                # print(arr)
                # print("done")
                with open(prev_tables+".csv", 'r') as f:
                    readCSV = csv.reader(f, delimiter=',')
                    for rows in readCSV:
                        # print(rows)
                        if(count==0):
                            lent=len(rows)
                            for i in range(lent):
                                if(rows[i]==pred):
                                    col=i
                                    # print(col) 
                                    # print(sign)
                                    # print(arr)   
                                    # print(value) 
                                    # print()
                                    # print("-------------")       
                        else:               
                            if sign=='=':
                                if(rows[col]!=value):
                                    arr[count-1]=0 
                            elif sign=='>':
                                # print(rows[col])
                                if rows[col] != "" and int(rows[col]) <= int(value):
                                    arr[count-1]=0 
                                    # print(arr[count-1])
                                    # print("Ppppppp")
                            elif(sign=='<'):
                                if rows[col] != "" and int(rows[col])>=int(value):
                                    arr[count-1]=0 

                            elif(sign=='>='):
                                if int(rows[col])<int(value):
                                    arr[count-1]=0 
                            else:
                                if int(rows[col])>int(value):
                                    arr[count-1]=0 ;
                        count+=1 
        for iii in range(1000*ppp,(1000*ppp+1000)):
            final_arr[iii]=arr[iii%1000]
        ppp+=1
    # print("done")
    f1=f1+1     
    xxx,counter_total=bitmaps(final_arr,int(siz1),counter_total)            
    final=final+str(xxx) #working tested
# print(final)
file1 = open("test.bitmaps","wb")
file1.write(binascii.unhexlify(''.join(final.split())))



                

