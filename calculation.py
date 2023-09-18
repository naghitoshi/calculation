import argparse
import re
import statistics

#サンプル分散
def culc_mean_and_sd():
    print("数値を入力して下さい")
    numeric_string = input("(カンマ区切りまたはスペース区切り)")
    if numeric_string == "":
        print("入力無し. 終了")
        return
    else:
        numbers = re.split ('[,\s]+', numeric_string)
        print(numbers)
        for i in range(len(numbers)):
            if isfloat(numbers[i]):
                numbers[i] = float(numbers[i])
            else:
                print("入力が不適切です。もう一度")
                return culc_mean_and_sd()
        print(f"{statistics.mean(numbers):.5f} ± {statistics.stdev(numbers):.5f} (平均 ± 標本標準偏差)")
    return

def isfloat(s):  # 浮動小数点数値かどうかを判定する関数
    try:
        float(s)  # 試しにfloat関数で文字列を変換
    except ValueError:
        return False  # 失敗すれば False
    else:
        return True  # 上手くいけば True

def main():
    culc_mean_and_sd()


if __name__ == "__main__":
    main()
