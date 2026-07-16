# LeetCode 0552 - Student Attendance Record II
# https://leetcode.com/problems/student-attendance-record-ii/


class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10**9 + 7
        # dp[absences][trailing_lates]
        dp = [[0, 0, 0] for _ in range(2)]
        dp[0][0] = 1

        for _ in range(n):
            nxt = [[0, 0, 0] for _ in range(2)]
            for absences in range(2):
                for lates in range(3):
                    ways = dp[absences][lates]
                    if ways == 0:
                        continue
                    # Present resets consecutive lates
                    nxt[absences][0] = (nxt[absences][0] + ways) % mod
                    # Absent (at most one total)
                    if absences == 0:
                        nxt[1][0] = (nxt[1][0] + ways) % mod
                    # Late (at most two consecutive)
                    if lates < 2:
                        nxt[absences][lates + 1] = (nxt[absences][lates + 1] + ways) % mod
            dp = nxt

        return sum(sum(row) for row in dp) % mod
