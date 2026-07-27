// LeetCode 1637 - Widest Vertical Area Between Two Points Containing No Points
// https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

class Solution {
    func maxWidthOfVerticalArea(_ points: [[Int]]) -> Int {
        let xs = points.map { $0[0] }.sorted()
        var ans = 0
        for i in 1..<xs.count {
            ans = max(ans, xs[i] - xs[i - 1])
        }
        return ans
    }
}
