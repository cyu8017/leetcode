// LeetCode 0956 - Tallest Billboard
// https://leetcode.com/problems/tallest-billboard/

class Solution {
    func tallestBillboard(_ rods: [Int]) -> Int {
        var dp = [0: 0]
        for rod in rods {
            let cur = dp
            for (diff, taller) in cur {
                let key1 = diff + rod
                dp[key1] = max(dp[key1] ?? 0, taller + rod)
                let nd = abs(diff - rod)
                let nt = diff >= rod ? taller : taller - diff + rod
                dp[nd] = max(dp[nd] ?? 0, nt)
            }
        }
        return dp[0] ?? 0
    }
}
