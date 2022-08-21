class Solution(object):
    def isValid(self, s):
        diccionary = {')': '(', ']': '[', '}':'{'}
        lista = []

        for i in s:
            if i in diccionary:
                if lista and lista[-1] == diccionary[i]:
                    lista.pop()
                else:
                    return False
            else:
                lista.append(i)
        return True if not lista else False
       

if __name__ == "__main__":
    s = "()[]"
    test = Solution()
    print(test.isValid(s))