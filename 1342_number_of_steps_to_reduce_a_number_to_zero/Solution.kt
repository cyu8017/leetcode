// LeetCode 1342 - Number of Steps to Reduce a Number to Zero
// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution {
    fun numberOfSteps(num: Int): Int {
        var n = num
        var steps = 0
        while (n > 0) {
            n = if (n % 2 == 0) n / 2 else n - 1
            steps++
        }
        return steps
    }
}
