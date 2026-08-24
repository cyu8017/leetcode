// LeetCode 3893 - Maximum Team Size With Overlapping Intervals
// https://leetcode.com/problems/maximum-team-size-with-overlapping-intervals/

class Solution {
    func maximumTeamSize(_ startTime: [Int], _ endTime: [Int]) -> Int {
        let n = startTime.count
        let st = startTime.sorted()
        let en = endTime.sorted()
        var ans = 0
        for t in 0..<n {
            let l = startTime[t], r = endTime[t]
            let i = upperBound(en, l - 1)
            let j = upperBound(st, r)
            ans = max(ans, j - i)
        }
        return ans
    }

    private func upperBound(_ a: [Int], _ x: Int) -> Int {
        var lo = 0, hi = a.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if a[mid] <= x { lo = mid + 1 }
            else { hi = mid }
        }
        return lo
    }
}
