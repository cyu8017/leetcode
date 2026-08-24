// LeetCode 2426 - Number of Pairs Satisfying Inequality
// https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution {
    private lateinit var arr: IntArray
    private lateinit var tmp: IntArray

    fun numberOfPairs(nums1: IntArray, nums2: IntArray, diff: Int): Long {
        val n = nums1.size
        arr = IntArray(n) { nums1[it] - nums2[it] }
        tmp = IntArray(n)
        return mergeCount(0, n, diff)
    }

    private fun mergeCount(l: Int, r: Int, diff: Int): Long {
        if (r - l <= 1) return 0
        val m = (l + r) / 2
        var ans = mergeCount(l, m, diff) + mergeCount(m, r, diff)
        var j = m
        for (i in l until m) {
            while (j < r && arr[j] < arr[i] - diff) j++
            ans += (r - j).toLong()
        }
        var p = l
        var q = m
        var i2 = l
        while (p < m && q < r) {
            if (arr[p] <= arr[q]) tmp[i2++] = arr[p++]
            else tmp[i2++] = arr[q++]
        }
        while (p < m) tmp[i2++] = arr[p++]
        while (q < r) tmp[i2++] = arr[q++]
        for (t in l until r) arr[t] = tmp[t]
        return ans
    }
}
