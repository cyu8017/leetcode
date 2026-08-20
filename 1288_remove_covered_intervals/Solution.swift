// LeetCode 1288 - Remove Covered Intervals
// https://leetcode.com/problems/remove-covered-intervals/

class Solution {
    func removeCoveredIntervals(_ intervals: [[Int]]) -> Int {
        let sorted = intervals.sorted { a, b in
            if a[0] != b[0] { return a[0] < b[0] }
            return a[1] > b[1]
        }
        var ans = 0, end = 0
        for iv in sorted {
            if iv[1] > end {
                ans += 1
                end = iv[1]
            }
        }
        return ans
    }
}
