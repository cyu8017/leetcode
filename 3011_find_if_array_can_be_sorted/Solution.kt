// LeetCode 3011 - Find if Array Can Be Sorted
// https://leetcode.com/problems/find-if-array-can-be-sorted/

class Solution {
    private fun popcount(x0: Int): Int {
        var x = x0
        var c = 0
        while (x != 0) {
            c += x and 1
            x = x shr 1
        }
        return c
    }

    fun canSortArray(nums: IntArray): Boolean {
        var preMx = 0
        var i = 0
        val n = nums.size
        while (i < n) {
            val cnt = popcount(nums[i])
            var j = i + 1
            var mi = nums[i]
            var mx = nums[i]
            while (j < n && popcount(nums[j]) == cnt) {
                mi = minOf(mi, nums[j])
                mx = maxOf(mx, nums[j])
                j++
            }
            if (preMx > mi) return false
            preMx = mx
            i = j
        }
        return true
    }
}
