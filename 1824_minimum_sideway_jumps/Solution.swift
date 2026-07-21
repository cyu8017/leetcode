// LeetCode 1824 - Minimum Sideway Jumps
// https://leetcode.com/problems/minimum-sideway-jumps/

class Solution {
    func minSideJumps(_ obstacles: [Int]) -> Int {
        let inf = Int.max / 4
        var dp = [1, 0, 1]
        for obs in obstacles {
            let blocked = (0..<3).map { obs == $0 + 1 }
            var ndp = [inf, inf, inf]
            for lane in 0..<3 where !blocked[lane] {
                for other in 0..<3 where !blocked[other] && dp[other] != inf {
                    ndp[lane] = min(ndp[lane], dp[other] + (lane != other ? 1 : 0))
                }
            }
            dp = ndp
        }
        return dp.min()!
    }
}
