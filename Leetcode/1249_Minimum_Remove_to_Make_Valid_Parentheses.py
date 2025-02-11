class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        counter = 0
        ans = []
        for i in range(0, len(s)):
            if s[i] == "(":
                counter += 1
                ans.append(s[i])
            elif s[i] == ")":
                if counter == 0:
                    continue
                counter -= 1
                ans.append(s[i])
            else:
                ans.append(s[i])
        print(ans)
        if counter > 0:
            i  = len(ans) - 1
            while (counter > 0):
                if ans[i] == "(":
                    ans[i] = ""
                    counter -= 1
                i -= 1
        return "".join(ans)

