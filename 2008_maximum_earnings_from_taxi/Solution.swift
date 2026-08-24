// LeetCode 2008 - Maximum Earnings From Taxi
// https://leetcode.com/problems/maximum-earnings-from-taxi/

class Solution {
    func maxTaxiEarnings(_ n: Int, _ rides: [[Int]]) -> Int {
        let rides = rides.sorted { $0[1] < $1[1] }
        let m = rides.count
        let ends = rides.map { $0[1] }
        var dp = [Int](repeating: 0, count: m + 1)
        for i in 0..<m {
            let start = rides[i][0], end = rides[i][1], tip = rides[i][2]
            let earn = end - start + tip
            var lo = 0, hi = m
            while lo < hi {
                let mid = (lo + hi) / 2
                if ends[mid] <= start { lo = mid + 1 }
                else { hi = mid }
            }
            dp[i + 1] = max(dp[i], earn + dp[lo])
        }
        return dp[m]
    }
}
