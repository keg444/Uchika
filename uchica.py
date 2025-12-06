def menu() -> int:
    functions = ["乗車駅選択", "チャージ機能"]
    print("\n【ウチダ電鉄　交通系ICカード検証システム】\n")
    for i in range(len(functions)):
        print(f"{i+1}: {functions[i]}")
    
    print("使用する機能を選択してください（終了する場合には99を入力）")
    # 入力チェック
    while True:
        try:
            input_func = int(input())
        except ValueError:
            print("正しい数値を入力してください．")
        else:
            if input_func not in range(1, len(functions)) and input_func != 99:
                print("正しい数値を入力してください．")
            break
    return input_func

def select_station() -> int:   # 辞書にしたほうが良くね？→参照が面倒になるかも
    stations = ["秋葉原", "山梨", "長野"]
    fares = [133, 4128, 7990]
    print("【乗車駅選択】\n")
    for i in range(len(stations)):
        print(f"{i+1}: {stations[i]}駅から : {fares[i]}円")
    print("\n乗車した駅を入力してください（キャンセルする場合には99を入力）")
    while True:
        # 入力チェック
        # 整数以外の入力に対応ここから
        try:
            destination = int(input())
        except ValueError:
            print("正しい数値を入力してください．")
        # ここまで
        else:
            if destination not in range(1, len(stations)+1) and destination != 99:
                print("正しい数値を入力してください．")
                continue
            if destination == 99:
                print("駅の選択をキャンセルしました．")
                return 0        
            break
    print(f"乗車駅は{stations[destination-1]}で料金は{fares[destination-1]}円です．")
    return fares[destination - 1]

def pay(balance: int, fare: int) -> int:  # charge=残高
    charge = 3000
    print(f"チャージ残高は{balance}円です．")
    if balance < fare:
        print("残高不足です．")
        while balance < fare:
            print(f"{charge}円自動チャージします．")
            balance += charge
    balance -= fare  # 精算
    print(f"精算後のチャージ残高は{balance}円です．")
    
    if balance < 500:
        print(f"残高が500円未満のため{charge}円自動チャージします．")
        balance += charge
        print(f"チャージ残高は{balance}円です．")
    return balance

def charge(balance: int) -> int:
    charges = []
    # チャージ金額一覧
    for i in range(1000, 11000, 1000):
        charges.append(i)
    print("【チャージ機能】\n")
    print(f"チャージ残高は{balance}円です．\n")
    for i in range(len(charges)):
        print(f"{i+1}: {charges[i]}円\n")
    print("チャージする金額を選択してください（キャンセルする場合には99を入力）")
    # 入力チェック
    while True:
        try:
            input_charge = int(input())
        except ValueError:
            print("正しい数値を入力してください．")
        else:
            if input_charge not in range(1, len(charges)+1) and input_charge != 99:
                print("正しい数値を入力してください．")
                continue
            if input_charge > 0 and input_charge < 11:
                print(f"{input_charge * 1000}円チャージします．")
                balance += input_charge * 1000
                print(f"チャージ残高は{balance}円です．")
            elif input_charge == 99:
                print("チャージをキャンセルしました．")
            break
    return balance

def main():
    balance = 500   # 残高を初期化
    while True:
        func = menu()
        if func == 1:
            fare = select_station()
            if fare != 0:
                balance = pay(balance, fare)
        elif func == 2:
            balance = charge(balance)
        elif func == 99:
            print("システムを終了します．")
            break

if __name__ == "__main__":
    main()