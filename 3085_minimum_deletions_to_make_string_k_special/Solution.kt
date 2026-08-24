// LeetCode 3085 - Minimum Deletions to Make String K-Special
// https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/

class Solution {
    fun minimumDeletions(word: String, k: Int): Int {
        var freq = IntArray(26)
        for (i in 0 until word.length) { freq[word[i] - 'a']++ }
        var nums = ArrayList<Int>()
        for (v in freq) { if (v > 0) nums.add(v) }
        var ans = word.length
        for (i in 0 until = word.length) {
            var cur = 0
            for (x in nums) {
                if (x < i) cur += x
                else if (x > i + k) cur += x - i - k
            }
            ans = minOf(ans, cur)
        }
        return ans
    }
}
