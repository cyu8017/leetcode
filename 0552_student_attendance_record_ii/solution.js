// LeetCode 0552 - Student Attendance Record II
// https://leetcode.com/problems/student-attendance-record-ii/

/**
 * @param {number} n
 * @return {number}
 */
var checkRecord = function(n) {
    const MOD = 1000000007;
    let dp = [[1, 0, 0], [0, 0, 0]];
    for (let day = 0; day < n; ++day) {
        const nxt = Array.from({ length: 2 }, () => Array(3).fill(0));
        for (let absences = 0; absences < 2; ++absences) {
            for (let lates = 0; lates < 3; ++lates) {
                const ways = dp[absences][lates];
                if (ways === 0) continue;
                nxt[absences][0] = (nxt[absences][0] + ways) % MOD;
                if (absences === 0) nxt[1][0] = (nxt[1][0] + ways) % MOD;
                if (lates < 2) nxt[absences][lates + 1] = (nxt[absences][lates + 1] + ways) % MOD;
            }
        }
        dp = nxt;
    }
    let total = 0;
    for (let absences = 0; absences < 2; ++absences) {
        for (let lates = 0; lates < 3; ++lates) {
            total = (total + dp[absences][lates]) % MOD;
        }
    }
    return total;
};
