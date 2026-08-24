// LeetCode 3366 - Minimum Array Sum
// https://leetcode.com/problems/minimum-array-sum/

class Solution {
    func minArraySum(_ nums: [Int], _ k: Int, _ op1: Int, _ op2: Int) -> Int {
        let inf = Int(1e18)
        var dp = Array(repeating: Array(repeating: inf, count: op2 + 1), count: op1 + 1)
        dp[0][0] = 0
        for x in nums {
            var ndp = Array(repeating: Array(repeating: inf, count: op2 + 1), count: op1 + 1)
            for a in 0...op1 {
                for b in 0...op2 {
                    if dp[a][b] == inf { continue }
                    tryCand(&ndp, dp[a][b], a, b, x)
                    if a < op1 { tryCand(&ndp, dp[a][b], a + 1, b, (x + 1) / 2) }
                    if b < op2 && x >= k { tryCand(&ndp, dp[a][b], a, b + 1, x - k) }
                    if a < op1 && b < op2 {
                        let v1 = (x + 1) / 2
                        if v1 >= k { tryCand(&ndp, dp[a][b], a + 1, b + 1, v1 - k) }
                        if x >= k { tryCand(&ndp, dp[a][b], a + 1, b + 1, (x - k + 1) / 2) }
                    }
                }
            }
            dp = ndp
        }
        var ans = inf
        for a in 0...op1 {
            for b in 0...op2 where dp[a][b] < ans { ans = dp[a][b] }
        }
        return ans
    }

    private func tryCand(_ ndp: inout [[Int]], _ base: Int, _ na: Int, _ nb: Int, _ v: Int) {
        if base + v < ndp[na][nb] { ndp[na][nb] = base + v }
    }
}
