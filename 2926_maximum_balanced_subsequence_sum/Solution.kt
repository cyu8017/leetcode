// LeetCode 2926 - Maximum Balanced Subsequence Sum
// https://leetcode.com/problems/maximum-balanced-subsequence-sum/

class Solution {
    private lateinit var bit: LongArray
    private val NEG_INF = -(1L shl 60)

    fun maxBalancedSubsequenceSum(nums: IntArray): Long {
        val n = nums.size
        val keys = IntArray(n)
        val uniq0 = ArrayList<Int>()
        for (i in 0 until n) {
            keys[i] = nums[i] - i
            uniq0.add(keys[i])
        }
        uniq0.sort()
        val uniq = ArrayList<Int>()
        for (v in uniq0) {
            if (uniq.isEmpty() || uniq[uniq.size - 1] != v) uniq.add(v)
        }
        bit = LongArray(uniq.size + 2) { NEG_INF }
        var ans = NEG_INF
        for (i in 0 until n) {
            val id = idxOf(uniq, keys[i])
            val best = query(id)
            var cur = nums[i].toLong()
            if (best > NEG_INF / 2) {
                val cand = best + nums[i]
                if (cand > cur) cur = cand
            }
            update(id, cur)
            if (cur > ans) ans = cur
        }
        return ans
    }

    private fun idxOf(uniq: List<Int>, v: Int): Int {
        var lo = 0
        var hi = uniq.size
        while (lo < hi) {
            val mid = (lo + hi) ushr 1
            if (uniq[mid] < v) lo = mid + 1 else hi = mid
        }
        return lo + 1
    }

    private fun update(i0: Int, value: Long) {
        var i = i0
        while (i < bit.size) {
            if (value > bit[i]) bit[i] = value
            i += i and -i
        }
    }

    private fun query(i0: Int): Long {
        var i = i0
        var best = NEG_INF
        while (i > 0) {
            if (bit[i] > best) best = bit[i]
            i -= i and -i
        }
        return best
    }
}
