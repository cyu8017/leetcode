// LeetCode 1016 - Binary String With Substrings Representing 1 To N
// https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/

class Solution {
    fun queryString(s: String, n: Int): Boolean {
        for (i in n downTo n / 2 + 1) {
            if (!s.contains(i.toString(2))) return false
        }
        return true
    }
}
