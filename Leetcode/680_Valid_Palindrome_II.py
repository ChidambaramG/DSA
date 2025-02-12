class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        left, right = 0, len(s) - 1

        while (left < right):
            if s[left] != s[right]:
                if checkPalindrome(s, left+1, right) or checkPalindrome(s, left, right-1):
                    return True
                else:
                    return False
            left += 1
            right -= 1
        return True
