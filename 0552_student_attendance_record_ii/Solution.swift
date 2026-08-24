// LeetCode 0552 - Student Attendance Record II
// https://leetcode.com/problems/student-attendance-record-ii/

class Solution {
    func checkRecord(_ n: Int) -> Int {
        let MOD = 1_000_000_007
        var dp = [[1, 0, 0], [0, 0, 0]]
        for _ in 0..<n {
            var nxt = [[0, 0, 0], [0, 0, 0]]
            for absences in 0..<2 {
                for lates in 0..<3 {
                    let ways = dp[absences][lates]
                    if ways == 0 { continue }
                    nxt[absences][0] = (nxt[absences][0] + ways) % MOD
                    if absences == 0 {
                        nxt[1][0] = (nxt[1][0] + ways) % MOD
                    }
                    if lates < 2 {
                        nxt[absences][lates + 1] = (nxt[absences][lates + 1] + ways) % MOD
                    }
                }
            }
            dp = nxt
        }
        var total = 0
        for absences in 0..<2 {
            for lates in 0..<3 {
                total = (total + dp[absences][lates]) % MOD
            }
        }
        return total
    }
}
