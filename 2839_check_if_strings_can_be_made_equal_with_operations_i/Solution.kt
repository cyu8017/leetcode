// LeetCode 2839 - Check if Strings Can be Made Equal With Operations I
// https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/

class Solution {
    fun canBeEqual(s1: String, s2: String): Boolean {
        val a = charArrayOf(s1[0], s1[2])
        val b = charArrayOf(s2[0], s2[2])
        val c = charArrayOf(s1[1], s1[3])
        val d = charArrayOf(s2[1], s2[3])
        a.sort()
        b.sort()
        c.sort()
        d.sort()
        return a.contentEquals(b) && c.contentEquals(d)
    }
}
