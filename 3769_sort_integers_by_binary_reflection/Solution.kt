// LeetCode 3769 - Sort Integers By Binary Reflection
// https://leetcode.com/problems/sort_integers_by_binary_reflection/

class Solution {
    fun sortByReflection(nums: IntArray): IntArray {
        val arr = Array(nums.size) { nums[it] }
        arr.sortWith { a, b ->
            val fa = f(a)
            val fb = f(b)
            if (fa != fb) fa.compareTo(fb) else a.compareTo(b)
        }
        for (i in nums.indices) nums[i] = arr[i]
        return nums
    }

    private fun f(x0: Int): Int {
        var x = x0
        var y = 0
        while (x != 0) {
            y = (y shl 1) or (x and 1)
            x = x shr 1
        }
        return y
    }
}
