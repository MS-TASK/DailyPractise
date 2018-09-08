import time

def main():
    f = None
    try:
        f = open('E:\\python\\DailyPractise\\test.txt','r',encoding='utf-8')
        print(f.read())

        with open('E:\\python\\DailyPractise\\test.txt','r',encoding='utf-8') as f:
            for line in f:
                print(line,end=" ")
                time.sleep(2)
        
        print()

        with open('E:\\python\\DailyPractise\\test.txt','r',encoding='utf-8') as f:
            lines = f.readlines()
        print(lines)
    except FileNotFoundError:
        print('not find file...')
    except UnicodeDecodeError:
        print('read file occur error...')
    finally:
        if f:
            f.close()

if __name__ == '__main__':
    main()
    