class Solution:
    def isThree(self, n: int) -> bool:
        root = int(n ** 0.5)
        if root * root != n or root < 2:
            return False
        i = 2
        while i * i <= root:
            if root % i == 0:
                return False
            i += 1
        return True
