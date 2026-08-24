// LeetCode 3745 - Maximize Expression of Three Elements
// https://leetcode.com/problems/maximize-expression-of-three-elements/

class Solution {
    fun maximizeExpressionOfThree(nums: IntArray): Int {
        val inf = 1  shl  30
        var a = -inf
        var b = -inf
        var c = inf
        for (x in nums) {
            if (x < c) c = x
            if (x >= a) { b = a; a = x; }
            else if (x > b) b = x
        }
        return a + b - c
    }
}
