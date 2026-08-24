// LeetCode 3816 - Lexicographically Smallest String After Deleting Duplicate Characters
// https://leetcode.com/problems/lexicographically_smallest_string_after_deleting_duplicate_characters/

class Solution {
    fun lexSmallestAfterDeletion(s: String): String {
        val cnt = IntArray(26)
        for (c in s) cnt[c - 'a']++
        val stk = StringBuilder()
        for (c in s) {
            while (stk.isNotEmpty() && stk[stk.length - 1] > c &&
                cnt[stk[stk.length - 1] - 'a'] > 1
            ) {
                cnt[stk[stk.length - 1] - 'a']--
                stk.deleteCharAt(stk.length - 1)
            }
            stk.append(c)
        }
        while (cnt[stk[stk.length - 1] - 'a'] > 1) {
            cnt[stk[stk.length - 1] - 'a']--
            stk.deleteCharAt(stk.length - 1)
        }
        return stk.toString()
    }
}
