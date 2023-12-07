
V={'V1':100, 'V2':130, 'V3':200, 'V4':230, 'V5':400, 'V6':330, 'V7':330}
N={'N1':400, 'N2':530, 'N3':300, 'N4':630, 'N5':200, 'N6':530, 'N7':650}
S={'S1':100, 'S2':70, 'S3':120, 'S4':200, 'S5':170, 'S6':220, 'S7':90}
#Enter customer details
name=input("Enter the custmoer name: ")
age=int(input("Enter customer age: "))
add=input("Enter custmoer address: ")


n1=int(input("enter no of veg dishes: "))
n2=int(input("enter no of non-veg dishes: "))
n3=int(input("enter no of sweet dishes: "))


VD=[]
ND=[]  
SD=[]

QV=[]
QN=[]
QS=[]
for x in range(n1):
    nm=input("Enter Veg dishes name: ")
    q=int(input("Enter Quantatiy: "))
    VD.append(nm)
    QV.append(q)

q=[]
for x in range(n2):
    nm=input("Enter Non-Veg dishes name: ")
    q=int(input("Enter Quantatiy: "))
    ND.append(nm)
    QN.append(q)


q=[]
for x in range(n3):
    nm=input("Enter Sweet dishes name: ")
    q=int(input("Enter Quantatiy: "))
    SD.append(nm)
    QS.append(q)

VP=[]
NP=[]
SP=[]

for x in VD:
    VP.append(V.get(x))

for x in ND:
    NP.append(N.get(x))

for x in SD:
    SP.append(S.get(x))

print(VD,ND,SD)
print(VP,NP,SP)

total_bill=0

for x in range(n1):
    total_bill=total_bill+(QV[x] * VP[x])

for x in range(n2):
    total_bill=total_bill+(QN[x] * NP[x])

for x in range(n3):
    total_bill=total_bill+(QS[x] * SP[x])

print(total_bill)