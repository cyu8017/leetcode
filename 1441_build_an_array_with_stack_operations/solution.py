class Solution:
    def buildArray(self, target, n):
        answer = []
        current = 1
        for value in target:
            while current < value:
                answer.extend(("Push", "Pop"))
                current += 1
            answer.append("Push")
            current += 1
        return answer
