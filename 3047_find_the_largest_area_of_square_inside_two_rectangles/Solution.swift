// LeetCode 3047 - Find the Largest Area of Square Inside Two Rectangles
// https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/

class Solution {
    func largestSquareArea(_ bottomLeft: [[Int]], _ topRight: [[Int]]) -> Int {
        var ans = 0
        let n = bottomLeft.count
        for i in 0..<n {
            let x1 = bottomLeft[i][0], y1 = bottomLeft[i][1]
            let x2 = topRight[i][0], y2 = topRight[i][1]
            for j in (i + 1)..<n {
                let x3 = bottomLeft[j][0], y3 = bottomLeft[j][1]
                let x4 = topRight[j][0], y4 = topRight[j][1]
                let ww = min(x2, x4) - max(x1, x3)
                let h = min(y2, y4) - max(y1, y3)
                let e = min(ww, h)
                if e > 0 { ans = max(ans, e * e) }
            }
        }
        return ans
    }
}
