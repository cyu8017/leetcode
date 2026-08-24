// LeetCode 0028 - Find the Index of the First Occurrence in a String
// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution {
    fun strStr(haystack: String, needle: String): Int {
        if (needle.isEmpty()) {
            return 0
        }

        val needleLen = needle.length
        for (i in 0..haystack.length - needleLen) {
            if (haystack.substring(i, i + needleLen) == needle) {
                return i
            }
        }

        return -1
    }
}
