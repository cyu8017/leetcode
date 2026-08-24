// LeetCode 3229 - Minimum Operations to Make Array Equal to Target
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/

class Solution {
    fun minimumOperations(nums: IntArray, target: IntArray): Long {
        var f = kotlin.math.abs(target[0] - nums[0])
        for (i in 1 until target.size) {
            var x = target[i] - nums[i]
            var y = target[i - 1] - nums[i - 1]
            if (x * y > 0) {
                var d = kotlin.math.abs(x) - kotlin.math.abs(y)
                if (d > 0) {
                    f += d
                }
            } else {
                f += kotlin.math.abs(x)
            }
        }
        return f
    }
}
