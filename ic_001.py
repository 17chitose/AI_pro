def menu():
  #ここに処理の中身を書く。()カッコ内の引数はある場合は書く。
  print("【ウチダ電鉄　交通系IC　カード検証システム】")
  print("")
  print("1：乗車機能選択")
  print("2：チャージ機能選択")
  print("")

  judge = False

  while  judge == False:
    select_fanction = input("使用する機能を入力してください：")
    if select_fanction == "1" or select_fanction == "１":
      select_fanction = 1
      judge = True
    elif select_fanction == "2" or select_fanction == "２":
      select_fanction = 2
      judge = True
    elif select_fanction == "99" or select_fanction == "９９":
      select_fanction = 99
      judge = True
    else:
       print("正しい数値を入力してください")
  
  return select_fanction

def select_station():
  #ここに処理の中身を書く。()カッコ内の引数はある場合は書く。
  pass #このpassは処理を書いた後消してよい。


def pay(balance, fare):
  #ここに処理の中身を書く。()カッコ内の引数はある場合は書く。
  if balance < fare:
    print("残高不足です。")

  while True:
    charge_money = 3000

    if balance < fare:
       balance += 3000
       print(f"{charge_money}円自動チャージします。")
    else:
       balance -= fare
       print(f"精算後のチャージ残高は{balance}円です。")
       return balance


def charge():
  #ここに処理の中身を書く。()カッコ内の引数はある場合は書く。
    charge_max = 10
    check_charge = False
    print(f"【チャージ機能】\nチャージ残高は {balance} 円です。")
    for i in range(1,charge_max+1):
        print(f"{i}: {i*1000}円")
    num = input("チャージする金額を選択してください。(キャンセルする場合には 99 を入力)")

    while True:
        for i in range(1,charge_max+1):
            if i == int(num):
                check_charge = True
    
        if check_charge:
            balance += int(num)*1000
            print(f"チャージ残高は {balance} 円です。")
            return balance
        elif int(num) == 99:
            print("チャージをキャンセルしました")
            print(f"チャージ残高は {balance} 円です。")
            return balance
        else: 
            num = input("正しい数値を入力してください。")


def main():
  balance = 500
  while True:
    select_function = menu()
    if select_function == 1:
      fare = select_station()
      balance = pay(balance,fare)
    elif select_function == 2:
      balance = charge()
    elif select_function == 99:
      break

if __name__ == "__main__":
    main()
