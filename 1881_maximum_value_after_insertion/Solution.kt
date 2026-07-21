// LeetCode 1881 - Maximum Value after Insertion
// https://leetcode.com/problems/maximum-value-after-insertion/

class Solution {
    fun maxValue(n: String, x: Int): String {
        val neg = n[0] == '-'
        val start = if (neg) 1 else 0
        for (i in start until n.length) {
            val d = n[i] - '0'
            if (neg) {
                if (d > x) return n.substring(0, i) + x + n.substring(i)
            } else {
                if (d < x) return n.substring(0, i) + x + n.substring(i)
            }
        }
        return n + x
    }
}
