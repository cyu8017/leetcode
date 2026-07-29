// LeetCode 1081 - Smallest Subsequence of Distinct Characters
// https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

class Solution {
    fun smallestSubsequence(s: String): String {
        val last = IntArray(26)
        for (i in s.indices) last[s[i] - 'a'] = i
        val stack = StringBuilder()
        val used = BooleanArray(26)
        for (i in s.indices) {
            val ch = s[i]
            if (used[ch - 'a']) continue
            while (stack.isNotEmpty() &&
                ch < stack[stack.lastIndex] &&
                last[stack[stack.lastIndex] - 'a'] > i
            ) {
                val top = stack[stack.lastIndex]
                stack.deleteCharAt(stack.lastIndex)
                used[top - 'a'] = false
            }
            stack.append(ch)
            used[ch - 'a'] = true
        }
        return stack.toString()
    }
}
