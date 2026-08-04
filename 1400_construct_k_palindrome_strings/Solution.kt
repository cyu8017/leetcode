// LeetCode 1400 - Construct K Palindrome Strings
// https://leetcode.com/problems/construct-k-palindrome-strings/

class Solution {
    fun canConstruct(s: String, k: Int): Boolean {
        if (k > s.length) return false
        val freq = IntArray(26)
        for (c in s) freq[c - 'a']++
        val odds = freq.count { it % 2 == 1 }
        return odds <= k
    }
}
