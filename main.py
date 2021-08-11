import pandas as pd


x=pd.read_csv("MultiIndexDemo.csv")
res=pd.DataFrame(x)
print(res)
print()
print("--------------------------------------------------------")
a=res[res.Dept == "CE"]
print(a)
print()
sem5=a[a.Sem==5]
print(sem5)
print("Average marks of subject 1 in sem-5: ",sem5['S1'].mean())
print("Average marks of subject 2 in sem-5: ",sem5['S2'].mean())
print("Average marks of subject 3 in sem-5: ",sem5['S3'].mean())

print()

sem7=a[a.Sem==7]
print(sem7)
print("Average marks of subject 1 in sem-7: ",sem7['S1'].mean())
print("Average marks of subject 2 in sem-7: ",sem7['S2'].mean())
print("Average marks of subject 3 in sem-7: ",sem7['S3'].mean())

print()
print("--------------------------------------------------------")
x=res[res.Col=="VGEC"]
print(x)
print()

sem5=x[x.Sem==5]
print(sem5)
print("Maximum marks of subject 1 in sem-5: ",sem5['S1'].max())
print("Maximum marks of subject 2 in sem-5: ",sem5['S2'].max())
print("Maximum marks of subject 3 in sem-5: ",sem5['S3'].max())

print()
sem7=x[x.Sem==7]
print(sem7)
print("Maximum marks of subject 1 in sem-7: ",sem7['S1'].max())
print("Maximum marks of subject 2 in sem-7: ",sem7['S2'].max())
print("Maximum marks of subject 3 in sem-7: ",sem7['S3'].max())

print("--------------------------------------------------------")

sem5=res[res.Sem==5]
print(sem5)
print("Average marks of subject 1 in sem-5: ",sem5['S1'].mean())
print("Average marks of subject 2 in sem-5: ",sem5['S2'].mean())
print("Average marks of subject 3 in sem-5: ",sem5['S3'].mean())
print()
sem7=res[res.Sem==7]
print(sem7)
print("Average marks of subject 1 in sem-7: ",sem7['S1'].mean())
print("Average marks of subject 2 in sem-7: ",sem7['S2'].mean())
print("Average marks of subject 3 in sem-7: ",sem7['S3'].mean())

print()
print("--------------------------------------------------------")

vgec=res[res.Col=="VGEC"]
print(vgec)
sem5=vgec[vgec.Sem==5]
print("Vgec: ")
print("Average marks of subject 1 in sem-5: ",sem5['S1'].mean())
print("Average marks of subject 2 in sem-5: ",sem5['S2'].mean())
print("Average marks of subject 3 in sem-5: ",sem5['S3'].mean())

print()
sem7=vgec[vgec.Sem==7]
print("Average marks of subject 1 in sem-7: ",sem7['S1'].mean())
print("Average marks of subject 2 in sem-7: ",sem7['S2'].mean())
print("Average marks of subject 3 in sem-7: ",sem7['S3'].mean())

print()

abc=res[res.Col=="ABC"]
print(abc)
sem5=abc[abc.Sem==5]
print("ABC: ")
print("Average marks of subject 1 in sem-5: ",sem5['S1'].mean())
print("Average marks of subject 2 in sem-5: ",sem5['S2'].mean())
print("Average marks of subject 3 in sem-5: ",sem5['S3'].mean())

print()
sem7=abc[abc.Sem==7]

print("Average marks of subject 1 in sem-7: ",sem7['S1'].mean())
print("Average marks of subject 2 in sem-7: ",sem7['S2'].mean())
print("Average marks of subject 3 in sem-7: ",sem7['S3'].mean())