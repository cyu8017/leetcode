// LeetCode 1576 - Replace All ?'s to Avoid Consecutive Repeating Characters
// https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

class Solution {
    fun modifyString(s: String): String {
        val chars = s.toCharArray()
        for (i in chars.indices) {
            if (chars[i] == '?') {
                var c = 'a'
                while (c <= 'c') {
                    if ((i == 0 || chars[i - 1] != c) && (i + 1 == chars.size || chars[i + 1] != c)) {
                        chars[i] = c
                        break
                    }
                    c++
                }
            }
        }
        return String(chars)
    }
}
