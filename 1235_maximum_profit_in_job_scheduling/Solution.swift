// LeetCode 1235 - Maximum Profit in Job Scheduling
// https://leetcode.com/problems/maximum-profit-in-job-scheduling/

class Solution {
    func jobScheduling(_ startTime: [Int], _ endTime: [Int], _ profit: [Int]) -> Int {
        let n = startTime.count
        var jobs = (0..<n).map { (startTime[$0], endTime[$0], profit[$0]) }
        jobs.sort { $0.1 < $1.1 }
        var dp = [Int](repeating: 0, count: n)
        for i in 0..<n {
            var lo = 0, hi = i
            while lo < hi {
                let mid = (lo + hi) / 2
                if jobs[mid].1 <= jobs[i].0 { lo = mid + 1 } else { hi = mid }
            }
            let bestPrev = lo > 0 ? dp[lo - 1] : 0
            dp[i] = max((i > 0 ? dp[i - 1] : 0), bestPrev + jobs[i].2)
        }
        return dp[n - 1]
    }
}
