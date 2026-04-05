import random

cash = 1000
print("欢迎来到骰子赌博游戏！")
print("规则：")
print("- 掷出7或11点赢")
print("- 掷出2、3或12点输")
print("- 其他点数需要继续掷，直到掷出7（输）或相同点数（赢）")
print("-" * 50)

while cash > 0:
    print('当前金额为：', cash)
    while True:
        try:
            bet = int(input('请输入下注金额：'))
            if bet <= 0:
                print('下注金额必须大于0')
                continue
            if bet <= cash:
                # 第一次掷骰子
                first_point = random.randint(1, 12)
                print('你掷出了', first_point, '点')
                if first_point == 7 or first_point == 11:
                    print('你赢了', bet, '元')
                    cash += bet
                elif first_point == 12 or first_point == 2 or first_point == 3:
                    print('你输了', bet, '元')
                    cash -= bet
                else:
                    print('你继续掷骰')
                    while True:
                        current_point = random.randint(1, 12)
                        print('你掷出了', current_point, '点')
                        if current_point == 7:
                            print('你输了', bet, '元')
                            cash -= bet
                            break
                        elif current_point == first_point:
                            print('你赢了', bet, '元')
                            cash += bet
                            break
                break  # 跳出内层循环，进行下一轮下注
            else:
                print('下注金额不能大于当前金额')
        except ValueError:
            print('请输入有效的数字')

print("游戏结束！你的最终金额为：", cash)
if cash > 1000:
    print("恭喜你赢了", cash - 1000, "元！")
elif cash < 1000:
    print("很遗憾，你输了", 1000 - cash, "元。")
else:
    print("你收支平衡，下次再来！")