class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        idx = {"type": 0, "color": 1, "name": 2}[ruleKey]
        return sum(item[idx] == ruleValue for item in items)
