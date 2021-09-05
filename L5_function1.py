#!/bin/python3.8

def temperature(vaule_c):
    return 1.8 * vaule_c + 32

if __name__ == "__main__":
    # print(f"攝氏10度轉華氏溫度{temperature(10)}")
    # print("----------------------------------")
    runagain = True
    while runagain:
        tempc = int(input("請輸入攝氏溫度: "))
        tempf = temperature(tempc)
        print(f"華氏溫度{tempf}")
        input_word = input("需要繼續執行嗎? 輸入N結束: ")
        if input_word.upper() == "N":
            runagain = False
        else:
            runagain = True
    print("程式結束")