// LeetCode 2354 - Number of Excellent Pairs
// https://leetcode.com/problems/number-of-excellent-pairs/

class Solution {
    fun countExcellentPairs(nums: IntArray, k: Int): Long {
        val uniq = HashSet<Int>()
        for (x in nums) uniq.add(x)
        val cnt = IntArray(32)
        for (x in uniq) cnt[Integer.bitCount(x)]++
        var ans = 0L
        for (i in 0 until 32) {
            for (j in 0 until 32) {
                if (i + j >= k) ans += cnt[i].toLong() * cnt[j]
            }
        }
        return ans
    }
}
