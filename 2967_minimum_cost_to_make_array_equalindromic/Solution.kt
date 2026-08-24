// LeetCode 2967 - Minimum Cost to Make Array Equalindromic
// https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/

class Solution {
    private fun makePal(x: Int): Int {
        val ch = x.toString().toCharArray()
        var i = 0
        var j = ch.size - 1
        while (i < j) {
            ch[j] = ch[i]
            i++
            j--
        }
        return String(ch).toInt()
    }

    private fun cost(nums: IntArray, p: Int): Long {
        var c = 0L
        for (v in nums) c += kotlin.math.abs(v.toLong() - p)
        return c
    }

    private fun reverseChars(hs: String): String {
        val rb = hs.toCharArray()
        var i = 0
        var j = rb.size - 1
        while (i < j) {
            val tmp = rb[i]
            rb[i] = rb[j]
            rb[j] = tmp
            i++
            j--
        }
        return String(rb)
    }

    fun minimumCost(nums: IntArray): Long {
        nums.sort()
        val n = nums.size
        val median = nums[n / 2]
        val candidates = ArrayList<Int>()
        candidates.add(makePal(median))
        val s = median.toString()
        val half = s.substring(0, (s.length + 1) / 2).toInt()
        for (d in -2..2) {
            val h = half + d
            if (h <= 0) continue
            val hs = h.toString()
            val pal = if (s.length % 2 == 0) {
                hs + reverseChars(hs)
            } else {
                val prefix = hs.substring(0, hs.length - 1)
                hs + reverseChars(prefix)
            }
            try {
                candidates.add(pal.toInt())
            } catch (_: NumberFormatException) {
            }
        }
        for (v in intArrayOf(1, 9, 11, 99, 101)) candidates.add(v)
        var ans = Long.MAX_VALUE / 4
        for (p in candidates) {
            if (p <= 0) continue
            ans = minOf(ans, cost(nums, p))
        }
        return ans
    }
}
