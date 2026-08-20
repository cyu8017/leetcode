// LeetCode 1131 - Maximum of Absolute Value Expression
// https://leetcode.com/problems/maximum-of-absolute-value-expression/

class Solution {
    func maxAbsValExpr(_ arr1: [Int], _ arr2: [Int]) -> Int {
        var ans = 0
        for (p, q) in [(1, 1), (1, -1), (-1, 1), (-1, -1)] {
            var mx = Int.min, mn = Int.max
            for i in 0..<arr1.count {
                let v = p * arr1[i] + q * arr2[i] + i
                mx = max(mx, v)
                mn = min(mn, v)
            }
            ans = max(ans, mx - mn)
        }
        return ans
    }
}
