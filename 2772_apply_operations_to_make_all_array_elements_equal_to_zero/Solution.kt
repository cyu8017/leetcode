// LeetCode 2772 - Apply Operations to Make All Array Elements Equal to Zero
// https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/

class Solution {
    fun checkArray(nums: IntArray, k: Int): Boolean {
        var n = nums.size
        var diff = IntArray(n + 1)
        var cur = 0
        for (i in 0 until n) {
            cur += diff[i]
            var need = nums[i] - cur
            if (need < 0) return false
            if (need > 0) {
                if (i + k > n) return false
                cur += need
                diff[i + k] -= need
            }
        }
        return true
    }
}
