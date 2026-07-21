class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        def to_min(t: str) -> int:
            h, m = map(int, t.split(":"))
            return h * 60 + m

        start, end = to_min(loginTime), to_min(logoutTime)
        if end < start:
            end += 24 * 60
        start = (start + 14) // 15 * 15
        end = end // 15 * 15
        return max(0, (end - start) // 15)
