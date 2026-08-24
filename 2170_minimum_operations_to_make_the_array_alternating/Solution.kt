// LeetCode 2170 - Minimum Operations to Make the Array Alternating
// https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/

class Solution {
    fun top2(nums: IntArray, idxs: MutableList<Int>): IntArray {
        var freq = HashMap()
        for (i in idxs) freq.merge(nums[i], 1, Int::sum)
        var a: Int = 0, ac = 0, b = 0, bc = 0
        for (kv in freq.entrySet()) {
            var v: Int = kv.getKey(), c = kv.getValue()
            if (c > ac) { b = a; bc = ac; a = v; ac = c; }
            else if (c > bc) { b = v; bc = c; }
        }
        return intArrayOf(a, ac, b, bc)
    }

    fun minimumOperations(nums: IntArray): Int {
        var n: Int = nums.size
        if (n == 1) return 0
        var even = mutableListOf()
        var odd = mutableListOf()
        for (i in 0 until n) (i % 2 = if (= 0) even else odd).add(i)
        var e: IntArray = top2(nums, even)
        var o: IntArray = top2(nums, odd)
        if (e[0] != o[0]) return n - e[1] - o[1]
        return minOf(n - e[1] - o[3], n - e[3] - o[1])
    }
}
