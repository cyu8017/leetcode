// LeetCode 3111 - Minimum Rectangles to Cover Points
// https://leetcode.com/problems/minimum-rectangles-to-cover-points/

class Solution {
    func minRectanglesToCoverPoints(_ points: [[Int]], _ w: Int) -> Int {
        let pts = points.sorted { $0[0] < $1[0] }
        var ans = 0, x1 = -1
        for p in pts {
            if p[0] > x1 {
                ans += 1
                x1 = p[0] + w
            }
        }
        return ans
    }
}
