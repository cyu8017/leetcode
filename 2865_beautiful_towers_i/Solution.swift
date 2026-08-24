// LeetCode 2865 - Beautiful Towers I
// https://leetcode.com/problems/beautiful-towers-i/

class Solution {
    func maximumSumOfHeights(_ heights: [Int]) -> Int {
        let n = heights.count
        var ans = 0
        for peak in 0..<n {
            var sum = heights[peak]
            var mn = heights[peak]
            if peak > 0 {
                for i in stride(from: peak - 1, through: 0, by: -1) {
                    mn = min(mn, heights[i])
                    sum += mn
                }
            }
            mn = heights[peak]
            if peak + 1 < n {
                for i in (peak + 1)..<n {
                    mn = min(mn, heights[i])
                    sum += mn
                }
            }
            ans = max(ans, sum)
        }
        return ans
    }
}
