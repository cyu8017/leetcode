// LeetCode 3706 - Maximum Distance Between Unequal Words in Array II
// https://leetcode.com/problems/maximum-distance-between-unequal-words-in-array-ii/

class Solution {
    fun maxDistance(words: Array<String>): Int {
        var n = words.size
        var ans = 0
        for (i in 0 until n) {
            if (words[i] != words[0]) ans = maxOf(ans, i + 1)
            if (words[i] != words[n - 1]) ans = maxOf(ans, n - i)
        }
        return ans
    }
}
