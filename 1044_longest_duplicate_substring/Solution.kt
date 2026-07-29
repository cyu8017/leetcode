// LeetCode 1044 - Longest Duplicate Substring
// https://leetcode.com/problems/longest-duplicate-substring/

class Solution {
    private val MOD = 1_000_000_007L
    private val BASE = 911382323L

    fun longestDupSubstring(s: String): String {
        val n = s.length
        val nums = IntArray(n) { s[it].code }
        var lo = 0; var hi = n - 1; var start = -1; var bestLen = 0
        while (lo <= hi) {
            val mid = (lo + hi) / 2
            val pos = search(s, nums, mid)
            if (pos >= 0) {
                start = pos
                bestLen = mid
                lo = mid + 1
            } else {
                hi = mid - 1
            }
        }
        return if (start < 0) "" else s.substring(start, start + bestLen)
    }

    private fun search(s: String, nums: IntArray, length: Int): Int {
        if (length == 0) return 0
        val n = nums.size
        var h = 0L; var power = 1L
        for (i in 0 until length) {
            h = (h * BASE + nums[i]) % MOD
            power = power * BASE % MOD
        }
        val seen = HashMap<Long, MutableList<Int>>()
        seen.getOrPut(h) { mutableListOf() }.add(0)
        for (i in 1..n - length) {
            h = (h * BASE - nums[i - 1] * power % MOD + MOD) % MOD
            h = (h + nums[i + length - 1]) % MOD
            val idxs = seen[h]
            if (idxs != null) {
                val cur = s.substring(i, i + length)
                for (j in idxs) {
                    if (s.substring(j, j + length) == cur) return i
                }
                idxs.add(i)
            } else {
                seen[h] = mutableListOf(i)
            }
        }
        return -1
    }
}
