// LeetCode 2524 - Maximum Frequency Score of a Subarray
// https://leetcode.com/problems/maximum-frequency-score-of-a-subarray/

class Solution {
    private val MOD = 1_000_000_007

    private fun modPow(a0: Long, e0: Long): Long {
        var a = a0 % MOD
        var e = e0
        var res = 1L
        while (e > 0) {
            if ((e and 1L) != 0L) res = res * a % MOD
            a = a * a % MOD
            e = e shr 1
        }
        return res
    }

    fun maxFrequencyScore(nums: IntArray, k: Int): Int {
        val freq = HashMap<Int, Int>()
        var score = 0L
        var best = 0L
        for (i in nums.indices) {
            score = add(freq, score, nums[i])
            if (i >= k) score = remove(freq, score, nums[i - k])
            if (i >= k - 1 && score > best) best = score
        }
        return best.toInt()
    }

    private fun add(freq: MutableMap<Int, Int>, score0: Long, x: Int): Long {
        var score = score0
        val c = freq.getOrDefault(x, 0)
        if (c > 0) score = (score - modPow(x.toLong(), c.toLong()) + MOD) % MOD
        freq[x] = c + 1
        return (score + modPow(x.toLong(), (c + 1).toLong())) % MOD
    }

    private fun remove(freq: MutableMap<Int, Int>, score0: Long, x: Int): Long {
        var score = score0
        val c = freq[x]!!
        score = (score - modPow(x.toLong(), c.toLong()) + MOD) % MOD
        if (c == 1) freq.remove(x)
        else {
            freq[x] = c - 1
            score = (score + modPow(x.toLong(), (c - 1).toLong())) % MOD
        }
        return score
    }
}
