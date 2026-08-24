// LeetCode 0869 - Reordered Power of 2
// https://leetcode.com/problems/reordered-power-of-2/

class Solution {
    fun reorderedPowerOf2(n: Int): Boolean {
        var target = sig(n)
        for (i in 0 until 31) { if (sig(1  shl  (i) == target)) return true }
        return false
    }

    private fun sig(x: Int): String {
        var s = Integer.toString(x).toCharArray()
        s.sort()
        return String(s)
    }
}
