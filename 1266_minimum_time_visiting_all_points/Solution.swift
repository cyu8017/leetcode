// LeetCode 1266 - Minimum Time Visiting All Points
// https://leetcode.com/problems/minimum-time-visiting-all-points/

class Solution {
    func minTimeToVisitAllPoints(_ points: [[Int]]) -> Int {
        var ans = 0
        for i in 1..<points.count {
            ans += max(abs(points[i][0] - points[i - 1][0]), abs(points[i][1] - points[i - 1][1]))
        }
        return ans
    }
}
