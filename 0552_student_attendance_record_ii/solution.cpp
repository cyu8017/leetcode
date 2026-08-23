// LeetCode 0552 - Student Attendance Record II
// https://leetcode.com/problems/student-attendance-record-ii/

#include <cstring>

class Solution {
public:
    int checkRecord(int n) {
        const int MOD = 1000000007;
        long long dp[2][3] = {{1, 0, 0}, {0, 0, 0}};

        for (int day = 0; day < n; ++day) {
            long long nxt[2][3] = {{0}};
            for (int absences = 0; absences < 2; ++absences) {
                for (int lates = 0; lates < 3; ++lates) {
                    long long ways = dp[absences][lates];
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
            std::memcpy(dp, nxt, sizeof(dp));
        }

        long long total = 0;
        for (int absences = 0; absences < 2; ++absences) {
            for (int lates = 0; lates < 3; ++lates) {
                total = (total + dp[absences][lates]) % MOD;
            }
        }
        return static_cast<int>(total);
    }
};
