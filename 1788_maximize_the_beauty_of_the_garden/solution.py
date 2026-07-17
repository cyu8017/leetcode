class Solution:
    def maximumBeauty(self, flowers):
        first = {}
        prefix = [0]
        for value in flowers:
            prefix.append(prefix[-1] + max(value, 0))
        best = float("-inf")
        for i, value in enumerate(flowers):
            if value in first:
                left = first[value]
                between = prefix[i] - prefix[left + 1]
                best = max(best, flowers[left] + flowers[i] + between)
            else:
                first[value] = i
        return best
