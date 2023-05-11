_x = """Mainaru Vetti Katti
 https://youtu.be/gBzgpoq86U8
 Jimikki Ponnu
 https://youtu.be/HfMTwkVQohM
 Dippam Dappam
 https://youtu.be/j64M3CACcr4
 Enjoy Enjaami
 https://youtu.be/eYq7WapuDLU
 Jolly O Gymkhana
 https://youtu.be/PhxfspwMdww
 Dharala Prabhu
 https://youtu.be/3ZKf8yMfTGM
 Mamakutty
 https://youtu.be/R6343uT7yt8
 Mehabooba
 https://youtu.be/A5P6EdPdwjc
 Megham Karukatha
 https://youtu.be/cEWwJxEq9Lg
 Tum Tum
 https://youtu.be/tYSrY4iPX6w
 Thaai Kelavi 
 https://youtu.be/7CajfS_iVQM
 Aval
 https://youtu.be/My_S68DAAPg
 The Life Of Ram
 https://youtu.be/6LD30ChPsSs
 Kadhaippoma
 https://youtu.be/DScFlfN9vDk
 Thozhi
 https://youtu.be/o169wQ_4-1w
 Mudhal Nee Mudivum Nee
 https://youtu.be/ATElufr0OiE
 Aathadi Aathadi
 https://youtu.be/Fa-n8vk30qE
 Kadhal Kappal
 https://youtu.be/JZa7U91EflE
 Thala Kodhum 
 https://youtu.be/YwVHHZNtdKU
 Thangamey
 https://youtu.be/fv-4okrCbLA
 Eena Meena Teeka
 https://youtu.be/W-RAUYomJho
 Aazhi Soozhndha
 https://youtu.be/UVYApsOcdtc
 Vaayadipetha Pulla
 https://youtu.be/O0-lHTw3nLU
 Vaa Vaathi
 https://youtu.be/592mNGkpYig
 Mayakkama
 https://youtu.be/CFDCurqOERU
 Unkoodave Porakkanum
 https://youtu.be/2ggLEMPvgdU
 Ennai Vittu
 https://youtu.be/_IyZAqdt93U
 Kambathu Ponnu
 https://youtu.be/KPDhwjmb11o
 Bae
 https://youtu.be/w7Fjxf62t8E
 Kayilae Aagasam
 https://youtu.be/hjuAufsWqs0"""

splited = _x.split("\n")

songName = splited[: :2]
linkName = splited[1: :2]
# print(songName)
# print(linkName)

import random

def produce(i_value):
    _val = songName[random.randint(0, (len(songName))-1)]
    if _val == i_value:
        produce(i_value)
    else:
        return _val.strip()

tmpRepeat=0
for i in songName:
    print(f"""b++;
window["q"+b] = "{i}"; //Ans{tmpRepeat+1}
window["q1"+b] = "{produce(i)}";
window["q2"+b] = "{produce(i)}";
window["q3"+b] = "{produce(i)}";
window["q4"+b] = "{produce(i)}";
window["li"+b] = '{linkName[tmpRepeat]}';
""")
    tmpRepeat+=1