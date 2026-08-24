// LeetCode 2729 - Check if The Number is Fascinating
// https://leetcode.com/problems/check-if-the-number-is-fascinating/

class Solution {
    fun isFascinating(n: Int): Boolean {
        var s = (n).toString() + (2 * n).toString() + (3 * n).toString()
        if (s.length != 9) return false
        var cnt = IntArray(10)
        for (c in s.toCharArray()) { cnt[c - '0']++ }
        if (cnt[0] != 0) return false
        for (i in 1 ..9) { if (cnt[i] != 1) return false }
        return true
    }
}
