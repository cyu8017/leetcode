// LeetCode 1433 - Check If a String Can Break Another String
// https://leetcode.com/problems/check-if-a-string-can-break-another-string/

class Solution {
    fun checkIfCanBreak(s1: String, s2: String): Boolean {
        val a = s1.toCharArray().sorted()
        val b = s2.toCharArray().sorted()
        val ge = a.indices.all { a[it] >= b[it] }
        val le = a.indices.all { a[it] <= b[it] }
        return ge || le
    }
}
