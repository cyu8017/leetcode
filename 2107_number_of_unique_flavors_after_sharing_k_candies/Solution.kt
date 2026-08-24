// LeetCode 2107 - Number of Unique Flavors After Sharing K Candies
// https://leetcode.com/problems/number-of-unique-flavors-after-sharing-k-candies/

class Solution {
    fun shareCandies(candies: IntArray, k: Int): Int {
        var n: Int = candies.size
        var freq = HashMap()
        for (c in candies) freq.merge(c, 1, Int::sum)
        if (k == 0) return freq.size
        for (i in 0 until k) {
            var c: Int = candies[i]
            if (freq.merge(c, -1, Int::sum) == 0) freq.remove(c)
        }
        var ans: Int = freq.size
        for (i in k until n) {
            freq.merge(candies[i - k], 1, Int::sum)
            var c: Int = candies[i]
            if (freq.merge(c, -1, Int::sum) == 0) freq.remove(c)
            ans = maxOf(ans, freq.size)
        }
        return ans
    }
}
