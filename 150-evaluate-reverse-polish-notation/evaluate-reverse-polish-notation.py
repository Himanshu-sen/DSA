class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ls = ['+', '-', '/', '*']
        x, y = 0, 0
        stack = []
        for i in tokens:
            if i in ls:
                x = int(stack.pop())
                y = int(stack.pop())
                if i == "+":
                    stack.append(x+y)
                elif i == "-":
                    stack.append(y-x)
                elif i == "/":
                    stack.append(int(float(y)/x))
                elif i == "*":
                    stack.append(x*y)    
            else:
                stack.append(int(i))
        return stack[-1]


        