// LeetCode 2188 - Minimum Time to Finish the Race
// https://leetcode.com/problems/minimum-time-to-finish-the-race/

class Solution {
    func minimumFinishTime(_ tires: [[Int]], _ changeTime: Int, _ numLaps: Int) -> Int {
        var minTime = [Int](repeating: 1 << 30, count: 20)
        for tire in tires {
            let f = tire[0], r = tire[1]
            var t = f, lap = f
            var x = 1
            while x < 20 && t < minTime[x] {
                minTime[x] = t
                lap *= r
                if lap > changeTime + f { break }
                t += lap
                x += 1
            }
        }
        var dp = [Int](repeating: 1 << 30, count: numLaps + 1)
        dp[0] = -changeTime
        for i in 1...numLaps {
            var j = 1
            while j <= i && j < 20 {
                dp[i] = min(dp[i], dp[i - j] + changeTime + minTime[j])
                j += 1
            }
        }
        return dp[numLaps]
    }
}
