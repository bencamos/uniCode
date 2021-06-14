#Python Calculator
#
#ICTPRG407 | Learning Activity 2
import operator
print("Python Calculator | ICTPRG407")

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod,
    '^' : operator.xor,
}

def calc(op1, oper, op2, opera=ops.get):
    op1, op2 = int(op1), int(op2)
    return opera(oper)(op1, op2)

while 1:
    acceptableOperator = ["/", "-", "%", "+", "^", "*"];
    op = "";
    num1 = "";
    num2 = "";
    calculate = 0;
    posTrack = 0;
    arrLength = 0;

    x = raw_input(">> ")
    arr = x.split(" ")
    for i in arr:
        arrLength += 1;
        num = i.isdigit();
        if num:
            if posTrack:
                num2 = i;
                calculate = 1;
                i = 0;
            else:
                num1 = i;
                posTrack = 1;
        elif i == "x":
            op = "*";
        elif i in acceptableOperator:
            op = i;
        else:
            calculate = 0;
            print("Invalid");

        if calculate:
            res = calc(num1, op, num2);
            if len(arr) == 3:
                print(res);
            else:
                num1 = res;
                calculate = 0;
                i = 0;
            if arrLength == len(arr):
                print(res);