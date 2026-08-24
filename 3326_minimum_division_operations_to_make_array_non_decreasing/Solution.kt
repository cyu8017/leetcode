// LeetCode 3326 - Minimum Division Operations to Make Array Non Decreasing
// https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing/

class Solution {
    private fun smallestProperDivisor(x: Int): Int {
        run {
            var d = 2
            while (d * d <= x) {
                if (x % d == 0) return d
                d++
            }
        }
        return x
    }

    fun minOperations(nums: IntArray): Int {
        var ops = 0
        for (i in nums.size - 2 downTo 0) {
            if (nums[i] <= nums[i + 1]) continue
            while (nums[i] > nums[i + 1]) {
                var d = smallestProperDivisor(nums[i])
                if (d == nums[i]) return -1
                nums[i] /= d
                ops++
                if (nums[i] > nums[i + 1] && smallestProperDivisor(nums[i]) == nums[i]) return -1
            }
        }
        return ops
    }
}
