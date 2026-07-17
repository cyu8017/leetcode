// LeetCode 1781 - Sum of Beauty of All Substrings
// https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

class Solution {
    fun beautySum(s: String): Int {
        var ans = 0
        for (i in s.indices) {
            val freq = IntArray(26)
            for (j in i until s.length) {
                freq[s[j] - 'a']++
                var lo = Int.MAX_VALUE
                var hi = 0
                for (count in freq) {
                    if (count > 0) {
                        lo = minOf(lo, count)
                        hi = maxOf(hi, count)
                    }
                }
                ans += hi - lo
            }
        }
        return ans
    }
}
