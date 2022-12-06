def conver_input(_input):
    _input = _input.split()
    nums = []
    opers = []

    for i in range(len(_input)):
        if _input[i] == "+" or _input[i] == "-" or _input[i] == "*" or _input[i] == "/":
            opers.append(_input[i])
        else:
            nums.append(int(_input[i]))

    return [nums, opers]


def calulator(_input):
    nums = conver_input(_input)[0]
    oper = conver_input(_input)[1]

    if len(nums)-1 != len(oper):
        return "ERROR"

    i = 0
    while i < len(oper):
        if oper[i] == "*":
            answer = nums[i] * nums[i+1]
            oper.pop(i)
            nums.pop(i+1)
            nums[i] = answer
            i -= 1
        elif oper[i] == "/":
            answer = nums[i] / nums[i + 1]
            oper.pop(i)
            nums.pop(i + 1)
            nums[i] = answer
            i -= 1

        i += 1

    i = 0
    while i < len(oper):
        if oper[i] == "+":
            answer = nums[i] + nums[i + 1]
            oper.pop(i)
            nums.pop(i + 1)
            nums[i] = answer
            i -= 1
        elif oper[i] == "-":
            answer = nums[i] - nums[i + 1]
            oper.pop(i)
            nums.pop(i + 1)
            nums[i] = answer
            i -= 1

        i += 1

    return nums[0]


def main():
    _input = input()
    num = calulator(_input)

    print(num)


if __name__ == "__main__":
    main()