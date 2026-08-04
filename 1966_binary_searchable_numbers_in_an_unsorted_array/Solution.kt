// LeetCode 1966
// https://leetcode.com/problems/binary-searchable-numbers-in-an-unsorted-array/

class Solution {
    fun binarySearchableNumbers(nums: IntArray): Int {
        val n = nums.size
        val ok = BooleanArray(n) { true }
        var mx = Int.MIN_VALUE
        for (i in nums.indices) {
            if (nums[i] < mx) ok[i] = false else mx = nums[i]
        }
        var mi = Int.MAX_VALUE
        for (i in n - 1 downTo 0) {
            if (nums[i] > mi) ok[i] = false else mi = nums[i]
        }
        return ok.count { it }
    }
}
