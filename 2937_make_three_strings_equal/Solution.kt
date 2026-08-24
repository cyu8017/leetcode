// LeetCode 2937 - Make Three Strings Equal
// https://leetcode.com/problems/make-three-strings-equal/

class Solution {
    fun findMinimumOperations(s1: String, s2: String, s3: String): Int {
        var n = minOf(s1.length, minOf(s2.length, s3.length))
        var i = 0
        while (i < n && s1[i] == s2[i] && s2[i] == s3[i]) i++
        if (i == 0) return -1
        return s1.length + s2.length + s3.length - 3 * i
    }
}
