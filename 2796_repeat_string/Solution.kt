// LeetCode 2796 - Repeat String
// https://leetcode.com/problems/repeat-string/
// JS-only problem; C# stand-in.

class Solution {
    fun replicate(str: String, times: Int): String {
        if (times <= 0) return ""
        var sb = StringBuilder(str.length * times)
        for (i in 0 until times) { sb.append(str) }
        return sb.toString()
    }
}
