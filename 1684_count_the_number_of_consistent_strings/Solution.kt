// LeetCode 1684 - Count the Number of Consistent Strings
// https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution {
    fun countConsistentStrings(allowed: String, words: Array<String>): Int {
        val a = BooleanArray(26)
        for (c in allowed) a[c - 'a'] = true
        var ans = 0
        for (w in words) {
            if (w.all { a[it - 'a'] }) ans++
        }
        return ans
    }
}
