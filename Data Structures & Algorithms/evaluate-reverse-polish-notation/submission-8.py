class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) <=1:
            return int(tokens[0])
        ops = ("+","-","*","/")
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in ops:
                stack.append(int(tokens[i]))
                continue
            val1 = stack.pop()
            val2 = stack.pop()
            print(val1, val2, tokens[i])
            match tokens[i]:
                case "+":
                    val1 += val2
                case "-":
                    val1 = val2-val1
                case "*":
                    val1 *= val2
                case "/":
                    val1 = int(val2/val1)
            stack.append(val1)
            print(stack)
        
        return stack[0]