sayi1 = int(input("ilk sayiyi giriniz: "))
sayi2 = int(input("ikinci sayiyi giriniz: "))
operator = input("islem seciniz (+,-,*,/): ")

if operator == "+":
    print("Sonuc:",sayi1+sayi2)
elif operator == "-":
    print("Sonuc:",sayi1-sayi2)
elif operator == "*":
    print("Sonuc:",sayi1*sayi2)
elif operator == "/":
    print("Sonuc:",sayi1/sayi2)
else:
    print("geçersiz işlem.")