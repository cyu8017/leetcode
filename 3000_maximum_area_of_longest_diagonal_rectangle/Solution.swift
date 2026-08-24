// LeetCode 3000 - Maximum Area of Longest Diagonal Rectangle
// https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/

class Solution {
    func areaOfMaxDiagonal(_ dimensions: [[Int]]) -> Int {
        var ans = 0, mx = 0
        for d in dimensions {
            let l = d[0], w = d[1]
            let t = l * l + w * w
            if mx < t {
                mx = t
                ans = l * w
            } else if mx == t {
                ans = max(ans, l * w)
            }
        }
        return ans
    }
}
