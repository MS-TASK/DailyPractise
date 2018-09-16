import os
import time

def main():
    content = '大圣，此去欲何? 踏南天碎凌霄！'
    while True:
        os.system('cls') # clear 屏幕显示内容
        print(content)

        time.sleep(0.2)
        content = content[1:] + content[0]

if __name__ == '__main__':
    main()