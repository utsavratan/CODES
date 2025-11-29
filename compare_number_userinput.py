def compare_numbers():
    a=int(input("chal pehla number bol : "))
    b=int(input("Chal ab jaldi se dusra bol : "))
    if a>b:
        return"Ye le ! Pehla wala bada hai dusre wale se"
    elif a<b:
        return"Ooho ! Pehla wala to chhota hai dusre wale se"
    else:
        return"Ooo Terii ! Dono barabaar haiii"
print(compare_numbers())