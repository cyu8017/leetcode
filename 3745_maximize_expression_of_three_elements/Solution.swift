// LeetCode 3745 - Maximize Expression of Three Elements
// https://leetcode.com/problems/maximize-expression-of-three-elements/

class Solution {
    func maximizeExpressionOfThree(_ nums: [Int]) -> Int {
        let inf = 1 << 30
        var a = -inf, b = -inf, c = inf
        for x in nums {
            if x < c { c = x }
            if x >= a { b = a; a = x }
            else if x > b { b = x }
        }
        return a + b - c
    }
}
