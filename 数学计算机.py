import math
import datetime
HISTORY_FILE = "calculator_history.txt"
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("除数不能为0")
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("负数不能开平方")
    return math.sqrt(a)

def save_history(expression, result):
    now = datetime.datetime.now()
    time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    record = f"[{time_str}] {expression} = {result}\n"
    try:
        f = open(HISTORY_FILE, "a", encoding="utf-8")
        f.write(record)
        f.close()
    except IOError:
        print("保存历史记录失败！")

def read_history():
    print("\n=== 计算历史记录 ===")
    try:
        f = open(HISTORY_FILE, "r", encoding="utf-8")
        lines = f.readlines()
        f.close()
        if len(lines) == 0:
            print("暂无历史记录")
        else:
            for i, line in enumerate(lines):
                print(f"{i + 1}. {line.strip()}")
    except FileNotFoundError:
        print("暂无历史记录（文件不存在）")
    except IOError:
        print("读取历史记录失败！")

def clear_history():
    try:
        f = open(HISTORY_FILE, "w", encoding="utf-8")
        f.write("")
        f.close()
        print("历史记录已清空！")
    except IOError:
        print("清空历史记录失败！")

def input_number(prompt):
    while True:
        try:
            num_str = input(prompt)
            num = float(num_str)
            return num
        except ValueError:
            print("输入无效，请输入一个数字！")

def show_menu():
    print("\n" + "=" * 40)
    print("       数学计算器")
    print("=" * 40)
    print("请选择运算：")
    print("1. 加法 (+)")
    print("2. 减法 (-)")
    print("3. 乘法 (×)")
    print("4. 除法 (÷)")
    print("5. 幂运算 (a^b)")
    print("6. 开平方 (√)")
    print("7. 查看历史记录")
    print("8. 清空历史记录")
    print("0. 退出程序")
    print("=" * 40)

def main():
    print("欢迎使用数学计算器！")
    while True:
        show_menu()
        choice = input("请输入选项（0-8）：")
        if choice == "0":
            print("感谢使用，再见！")
            break
        elif choice == "1":
            print("\n--- 加法运算 ---")
            try:
                a = input_number("请输入第一个数：")
                b = input_number("请输入第二个数：")
                result = add(a, b)
                expr = f"{a} + {b}"
                print(f"结果：{expr} = {result}")
                save_history(expr, result)
            except Exception as e:
                print(f"出错了：{e}")
        elif choice == "2":
            print("\n--- 减法运算 ---")
            try:
                a = input_number("请输入第一个数：")
                b = input_number("请输入第二个数：")
                result = subtract(a, b)
                expr = f"{a} - {b}"
                print(f"结果：{expr} = {result}")
                save_history(expr, result)
            except Exception as e:
                print(f"出错了：{e}")
        elif choice == "3":
            print("\n--- 乘法运算 ---")
            try:
                a = input_number("请输入第一个数：")
                b = input_number("请输入第二个数：")
                result = multiply(a, b)
                expr = f"{a} × {b}"
                print(f"结果：{expr} = {result}")
                save_history(expr, result)
            except Exception as e:
                print(f"出错了：{e}")
        elif choice == "4":
            print("\n--- 除法运算 ---")
            try:
                a = input_number("请输入被除数：")
                b = input_number("请输入除数：")
                result = divide(a, b)
                expr = f"{a} ÷ {b}"
                print(f"结果：{expr} = {result}")
                save_history(expr, result)
            except ZeroDivisionError as e:
                print(f"错误：{e}")
            except Exception as e:
                print(f"出错了：{e}")
        elif choice == "5":
            print("\n--- 幂运算 ---")
            try:
                a = input_number("请输入底数：")
                b = input_number("请输入指数：")
                result = power(a, b)
                expr = f"{a} ^ {b}"
                print(f"结果：{expr} = {result}")
                save_history(expr, result)
            except Exception as e:
                print(f"出错了：{e}")
        elif choice == "6":
            print("\n--- 开平方运算 ---")
            try:
                a = input_number("请输入要开平方的数：")
                result = square_root(a)
                expr = f"√{a}"
                print(f"结果：{expr} = {result}")
                save_history(expr, result)
            except ValueError as e:
                print(f"错误：{e}")
            except Exception as e:
                print(f"出错了：{e}")
        elif choice == "7":
            read_history()
        elif choice == "8":
            confirm = input("确定要清空所有历史记录吗？(y/n)：")
            if confirm == "y" or confirm == "Y":
                clear_history()
            else:
                print("已取消清空操作")
        else:
            print("输入无效，请输入0-8之间的数字！")

if __name__ == "__main__":
    main()
