from operator import add
from operator import sub
from operator import mul
from operator import truediv

from array_stack import ArrayStack


def cal_simple_expression(exp):
    """只有+-*/四种运算, 运算数为整数, 运算符前后有空格."""
    end = '<'  # 表达式结束标志, 最低优先级
    priority = {end: 0, '+': 1, '-': 1, '*': 2, '/': 2}
    operator_func = {'+': add, '-': sub, '*': mul, '/': truediv}

    operand = ArrayStack()
    operator = ArrayStack()

    exp = exp.split()
    exp.append(end)  # 添加表达式结束标志以计算最终结果

    for i in exp:
        if i not in priority.keys():
            operand.push(int(i))
        else:
            if operator.is_empty() or priority[i] > priority[operator.top()]:
                operator.push(i)
            else:
                func = operator_func[operator.pop()]
                num1 = operand.pop()
                num2 = operand.pop()
                operand.push(func(num2, num1))

    return operand.pop()


# def cal_expression(exp):
#     """只有+-*/四种运算."""
#     priority = {'*': 1, '/': 1, '+': 2, '-': 2}
#     operand = ArrayStack()
#     operator = ArrayStack()
#
#     num = ''
#
#     for i in exp:
#         if i not in priority.keys():
#             num += i
#         else:
#             operand.push(int(num))
#             num = ''
#
#             if priority[i] > priority[operator.top()]:
#                 operator.push(i)
#             else:


if __name__ == '__main__':
    print(cal_simple_expression('3 + 5 * 8 - 6'))
    print(cal_simple_expression('5 / 2 - 1'))
    print(cal_simple_expression('10 / 3'))
