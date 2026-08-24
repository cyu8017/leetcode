// LeetCode 2566 - Maximum Difference by Remapping a Digit
// https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/

class Solution {
    fun minMaxDifference(num: Int): Int {
        val s = num.toString()
        var maxV = num
        for (c in s) {
            if (c != '9') {
                maxV = remap(s, c, '9')
                break
            }
        }
        val minV = remap(s, s[0], '0')
        return maxV - minV
    }

    private fun remap(s: String, from: Char, to: Char): Int {
        var v = 0
        for (c in s) {
            val d = if (c == from) to else c
            v = v * 10 + (d - '0')
        }
        return v
    }
}
