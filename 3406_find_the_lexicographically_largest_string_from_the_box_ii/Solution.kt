// LeetCode 3406 - Find the Lexicographically Largest String From the Box II
// https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-ii/

class Solution {
    fun answerString(word: String, numFriends: Int): String {
        if (numFriends == 1) return word
        var n = word.length
        var maxLen = n - (numFriends - 1)
        var ans = ""
        for (i in 0 until n) {
            var end = i + maxLen
            if (end > n) end = n
            var cand = word.substring(i, end)
            if (cand.compareTo(ans) > 0) ans = cand
        }
        return ans
    }
}
