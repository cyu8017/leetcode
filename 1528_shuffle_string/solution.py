# LeetCode 1528

class Solution:
    def restoreString(self, s, indices):
        answer = [""] * len(s)
        for ch, index in zip(s, indices):
            answer[index] = ch
        return "".join(answer)
