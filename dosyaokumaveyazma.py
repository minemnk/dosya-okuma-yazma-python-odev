dosya=open("deniyoruz.txt","w") 
girdi= input("Bir metin giriniz: ") 
dosya.write(girdi)  
dosya.close()

dosya=open("deniyoruz.txt" ,"r")
icerik=dosya.read()
print(icerik+"\n")
dosya.close()

dosya=open("deniyoruz.txt","a")
for i in range(5):
  girdi= input(f"{i} . satiri giriniz : ")
  dosya.write("\n" + girdi + "\n")
 
dosya=open("deniyoruz.txt","r")
for satir in dosya:
  print(satir)

dosya.close()