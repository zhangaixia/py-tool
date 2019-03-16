#!python3
#这是一个计算器，用于计算粘贴板中的数字
import re,sys,pyperclip,os
numre=re.compile(r'\d+[.]*\d*')#利用正则表达式提取粘贴板中的数字
saveadress=r'C:\Users\Administrator\Desktop\outcome.txt'#结果保存的路径
symbol=sys.argv[1]#获取运行的第二个参数 如CP +代表运行CP.bat 输入符号为+
outcometype={'+':'字符串中数字和为',
             'avg':'字符串中数字平均数为',
             'max':'字符串中最大数为',
             'min':'字符串中最小数为'}
def getnumber():
    numstr=pyperclip.paste()
    slist=numre.findall(numstr)
    nlist=[]
    if slist==[]:
        print('需粘贴正确的需要计算的数据')
        sys.exit()
    else:
        for i in slist:
            nlist.append(eval(i))
        return nlist
def symbolswitch(symbol,nlist):
    if symbol=='+':
        o=alladd(nlist)
    elif symbol=='avg':
        o=allaveage(nlist)
    elif symbol=='max':
        o=getmax(nlist)
    elif symbol=='min':
        o=getmin(nlist)
    else:
        print('你输入的符号不存在')
        sys.exit()
    return o
def saveoutcome(o,symbol):
    str1=outcometype[symbol]+str(o)+'已复制到粘贴板'
    pyperclip.copy(o)
    print(str1)
    print()
    txt=open(saveadress,'w')
    txt.write(str1)
    txt.close()
    os.system(saveadress)
def alladd(nlist):
    sumall=0
    for i in nlist:
        sumall+=i
    return sumall
def allaveage(nlist):
    return alladd(nlist)/len(nlist)
def getmax(nlist):
    return max(nlist)
def getmin(nlist):
    return min(nlist)
nlist=getnumber()
o=symbolswitch(symbol,nlist)
saveoutcome(o,symbol)

    
