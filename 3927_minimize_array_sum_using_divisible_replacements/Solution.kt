// LeetCode 3927 - Minimize Array Sum Using Divisible Replacements
// https://leetcode.com/problems/minimize-array-sum-using-divisible-replacements/

class Solution {
    fun minArraySum(nums: IntArray): Long {
        var maximum = 0
        val present = BooleanArray(100001)
        for (value in nums) {
            present[value] = true
            if (value > maximum) maximum = value
        }
        val best = IntArray(maximum + 1)
        for (divisor in 1..maximum) {
            if (!present[divisor]) continue
            var multiple = divisor
            while (multiple <= maximum) {
                if (best[multiple] == 0) best[multiple] = divisor
                multiple += divisor
            }
        }
        var answer = 0L
        for (value in nums) answer += best[value]
        return answer
    }
}
