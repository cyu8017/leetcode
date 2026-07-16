class Solution:
    def getHappyString(self, n, k):
        answer = []
        def build(path):
            if len(path) == n:
                answer.append(path)
                return
            for char in "abc":
                if not path or path[-1] != char:
                    build(path + char)
        build("")
        return answer[k - 1] if k <= len(answer) else ""
