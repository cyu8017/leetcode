// LeetCode 1957
// https://leetcode.com/problems/delete-characters-to-make-fancy-string/

class Solution {
    fun makeFancyString(s: String): String {
        val ans = StringBuilder()
        for (c in s) {
            if (ans.length >= 2 && ans[ans.length - 1] == c && ans[ans.length - 2] == c) continue
            ans.append(c)
        }
        return ans.toString()
    }
}
