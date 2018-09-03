#coding = utf-8
# def hanoi(n, x, y, z):
#     if n == 1:
#         print(x, '-->', z)
#     else:
#         hanoi(n-1, x, z, y)#将前n-1个盘子从x移动到y上
#         hanoi(1, x, y, z)#将最底下的最后一个盘子从x移动到z上
#         hanoi(n-1, y, x, z)#将y上的n-1个盘子移动到z上
# n=int(input('请输入汉诺塔的层数：'))
# hanoi(n, 'x', 'y', 'z')

def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1, fromPole, withPole, toPole)#move height-1 tower from fromPole to withPole
        moveDisk(fromPole, toPole) #move the last tower from fromPole to withPole
        moveTower(height-1, withPole, toPole, fromPole)#move height-1 tower in toPole to withPole

def moveDisk(fp,tp):
    print("moving disk from", fp, "to", tp)

def main():
    n = int(input('please input hanoi tower height:'))
    moveTower(n, 'A', 'B', 'C')

if __name__ == "__main__":
    main()