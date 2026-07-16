class Solution:
    def minNumberOfFrogs(self, croakOfFrogs):
        order = {char: i for i, char in enumerate("croak")}
        counts = [0] * 5
        active = answer = 0
        for char in croakOfFrogs:
            i = order.get(char, -1)
            if i < 0 or (i and counts[i - 1] == 0):
                return -1
            if i:
                counts[i - 1] -= 1
            counts[i] += 1
            if i == 0:
                active += 1
                answer = max(answer, active)
            elif i == 4:
                counts[4] -= 1
                active -= 1
        return answer if active == 0 else -1
