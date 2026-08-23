// LeetCode 0552 - Student Attendance Record II
// https://leetcode.com/problems/student-attendance-record-ii/

class Solution {
    public int checkRecord(int n) {
        final int MOD = 1000000007;
        long[][] dp = new long[][] {{1, 0, 0}, {0, 0, 0}};

        for (int day = 0; day < n; ++day) {
            long[][] nxt = new long[2][3];
            for (int absences = 0; absences < 2; ++absences) {
                for (int lates = 0; lates < 3; ++lates) {
                    long ways = dp[absences][lates];
                    if (ways == 0) {
                        continue;
                    }
                    nxt[absences][0] = (nxt[absences][0] + ways) % MOD;
                    if (absences == 0) {
                        nxt[1][0] = (nxt[1][0] + ways) % MOD;
                    }
                    if (lates < 2) {
                        nxt[absences][lates + 1] = (nxt[absences][lates + 1] + ways) % MOD;
                    }
                }
            }
            dp = nxt;
        }

        long total = 0;
        for (int absences = 0; absences < 2; ++absences) {
            for (int lates = 0; lates < 3; ++lates) {
                total = (total + dp[absences][lates]) % MOD;
            }
        }
        return (int) total;
    }
}
