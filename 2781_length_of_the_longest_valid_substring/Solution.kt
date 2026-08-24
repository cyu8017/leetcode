// LeetCode 2781 - Length of the Longest Valid Substring
// https://leetcode.com/problems/length-of-the-longest-valid-substring/

class Solution {
    fun longestValidSubstring(word: String, forbidden: MutableList<String>): Int {
        val forbid = HashSet<String>()
        var maxLen = 0
        for (f in forbidden) {
            forbid.add(f)
            maxLen = maxOf(maxLen, f.length)
        }
        var ans = 0
        var right = word.length - 1
        for (left in word.length - 1 downTo 0) {
            var k = left
            while (k <= right && k - left + 1 <= maxLen) {
                if (forbid.contains(word.substring(left, k + 1))) {
                    right = k - 1
                    break
                }
                k++
            }
            ans = maxOf(ans, right - left + 1)
        }
        return ans
    }
}
