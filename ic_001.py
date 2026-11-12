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
  print("【乗車駅選択】")
  print("")
  print("1：秋葉原駅から　　133円")
  print("2：山梨駅から　　4128円")
  print("3：長野駅から　　7990円")
  print("")

  judge = False
  fare = 0
  
  while  judge == False:
    select_station = input("乗車した駅を入力してください：")
    if select_station == "1" or select_station == "１":
      select_station = 1
      judge = True
    elif select_station == "2" or select_station == "２":
      select_station = 2
      judge = True
    elif select_station == "3" or select_station == "３":
      select_station = 3
      judge = True
    elif select_station == "99" or select_station == "９９":
      select_station = 99
      judge = True
    else:
      print("正しい数値を入力してください")

    if select_station == 1:
      fare = 133
      return fare
    elif select_station == 2:
      fare = 4128
      return fare
    elif select_station == 3:
      fare = 7990
      return fare
    elif select_station == 99:
      fare = 0
      return fare


def pay(balance, fare):
  #ここに処理の中身を書く。()カッコ内の引数はある場合は書く。
  print(f"チャージ残高は{balance}円です")

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
       break

  if balance < 500:
     print("残高が500円未満のため3000円自動チャージします。")
     balance += 3000
     print(f"チャージ残高は{balance}円です。")
     return balance
  else:
     return balance




def charge(balance):
  #ここに処理の中身を書く。()カッコ内の引数はある場合は書く。
    charge_max = 10
    check_charge = False
    print(f"【チャージ機能】\nチャージ残高は {balance} 円です。")
    for i in range(1,charge_max+1):
        print(f"{i}: {i*1000}円")
    num = input("チャージする金額を選択してください。(キャンセルする場合には 99 を入力)")

    while True:
        if num.isdecimal():
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
        else: 
            num = input("正しい数値を入力してください。")

def main():
  balance = 500
  while True:
    select_function = menu()
    if select_function == 1:
      fare = select_station()
      if fare == 0:
        print("駅の選択をキャンセルしました")
      else:
        balance = pay(balance,fare)
    elif select_function == 2:
      balance = charge(balance)
    elif select_function == 99:
      print("システムを終了します")
      break

if __name__ == "__main__":
    main()
