# LeetCode 1520

class Solution:
    def maxNumOfSubstrings(self, s):
        first = {ch: i for i, ch in reversed(list(enumerate(s)))}
        last = {ch: i for i, ch in enumerate(s)}
        intervals = []
        for i, ch in enumerate(s):
            if first[ch] != i:
                continue
            end = last[ch]
            j = i
            valid = True
            while j <= end:
                if first[s[j]] < i:
                    valid = False
                    break
                end = max(end, last[s[j]])
                j += 1
            if valid:
                intervals.append((end, i))
        intervals.sort()
        answer, previous_end = [], -1
        for end, start in intervals:
            if start > previous_end:
                answer.append(s[start:end + 1])
                previous_end = end
        return sorted(answer, key=len)
