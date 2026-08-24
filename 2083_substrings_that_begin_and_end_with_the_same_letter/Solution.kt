// LeetCode 2083 - Substrings That Begin and End With the Same Letter
// https://leetcode.com/problems/substrings-that-begin-and-end-with-the-same-letter/

class Solution {
    fun numberOfSubstrings(s: String): Long {
var freq: LongArray = LongArray(26)
var ans: Long = 0
for (char c : s.toCharArray()) {
freq[c - 'a']++
ans += freq[c - 'a']
}
return ans
}
}
