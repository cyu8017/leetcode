// LeetCode 3016 - Minimum Number of Pushes to Type Word II
// https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution {
    fun minimumPushes(word: String): Int {
        var cnt = IntArray(26)
        for (i in 0 until word.length) { cnt[word[i] - 'a']++ }
        cnt.sort()
        var ans = 0
        for (i in 0 until 26) { ans += (i / 8 + 1) * cnt[26 - i - 1] }
        return ans
    }
}
