// LeetCode 2191 - Sort the Jumbled Numbers
// https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution {
    private fun mapVal(mapping: IntArray, x0: Int): Int {
        if (x0 == 0) return mapping[0]
        var x = x0
        val digits = mutableListOf<Int>()
        while (x > 0) {
            digits.add(x % 10)
            x /= 10
        }
        var res = 0
        for (i in digits.size - 1 downTo 0) res = res * 10 + mapping[digits[i]]
        return res
    }

    fun sortJumbled(mapping: IntArray, nums: IntArray): IntArray {
        val n = nums.size
        val arr = Array(n) { intArrayOf(mapVal(mapping, nums[it]), it, nums[it]) }
        arr.sortWith(compareBy({ it[0] }, { it[1] }))
        return IntArray(n) { arr[it][2] }
    }
}
