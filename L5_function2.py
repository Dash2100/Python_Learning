import random
def lotGrnerator():
    lot = set()
    while len(lot) != 7:
        lot.add(random.randint(1, 49))

    print("本期大樂透電腦選號號碼如下: ")
    lotList = list(lot)
    specialNum = lotList.pop()
    for item in sorted(lotList):
        print(item, end="  ")
    print()
    print(f"特別號是{specialNum}")
    print("----------------------------")

if __name__ == "__main__":
    print("-- 大透透自動選號系統 --")
    print("=====================")
    input_word = int(input("請輸入組數: "))
    print("----------------------------")
    for i in range(0,input_word):
        print(f"第{i+1}組")
        lotGrnerator()