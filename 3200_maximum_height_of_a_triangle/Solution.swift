// LeetCode 3200 - Maximum Height of a Triangle
// https://leetcode.com/problems/maximum-height-of-a-triangle/

class Solution {
    func maxHeightOfTriangle(_ red: Int, _ blue: Int) -> Int {
        var ans = 0
        for k in 0..<2 {
            var c = [red, blue]
            var i = 1, j = k
            while i <= c[j] {
                c[j] -= i
                ans = max(ans, i)
                i += 1
                j ^= 1
            }
        }
        return ans
    }
}
