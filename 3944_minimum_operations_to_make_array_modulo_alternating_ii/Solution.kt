// LeetCode 3944 - Minimum Operations to Make Array Modulo Alternating II
// https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-ii/

class Solution {
    fun minOperations(nums: IntArray, k: Int): Long {
        val evenFreq = LongArray(k)
        val oddFreq = LongArray(k)
        for (i in nums.indices) {
            if (i % 2 == 0) evenFreq[nums[i] % k]++ else oddFreq[nums[i] % k]++
        }
        val evenCost = costs(evenFreq, k)
        val oddCost = costs(oddFreq, k)
        var best1 = 1L shl 62
        var best2 = 1L shl 62
        var bestIndex = -1
        for (i in 0 until k) {
            val x = oddCost[i]
            if (x < best1) {
                best2 = best1
                best1 = x
                bestIndex = i
            } else if (x < best2) best2 = x
        }
        var ans = 1L shl 62
        for (x in 0 until k) {
            val other = if (x == bestIndex) best2 else best1
            ans = minOf(ans, evenCost[x] + other)
        }
        return ans
    }

    private fun costs(freq: LongArray, k: Int): LongArray {
        val dbl = LongArray(2 * k)
        for (i in 0 until 2 * k) dbl[i] = freq[i % k]
        val countPrefix = LongArray(2 * k + 1)
        val weightedPrefix = LongArray(2 * k + 1)
        for (i in 0 until 2 * k) {
            countPrefix[i + 1] = countPrefix[i] + dbl[i]
            weightedPrefix[i + 1] = weightedPrefix[i] + i.toLong() * dbl[i]
        }
        val res = LongArray(k)
        val cw = k / 2
        val cc = (k - 1) / 2
        for (t in 0 until k) {
            val cnt = countPrefix[t + cw + 1] - countPrefix[t]
            val sum = weightedPrefix[t + cw + 1] - weightedPrefix[t]
            res[t] += sum - t.toLong() * cnt
            if (cc > 0) {
                val cnt2 = countPrefix[t + k] - countPrefix[t + k - cc]
                val sum2 = weightedPrefix[t + k] - weightedPrefix[t + k - cc]
                res[t] += (t + k).toLong() * cnt2 - sum2
            }
        }
        return res
    }
}
