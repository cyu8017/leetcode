// LeetCode 1681 - Minimum Incompatibility
// https://leetcode.com/problems/minimum-incompatibility/

class Solution {
    fun minimumIncompatibility(nums: IntArray, k: Int): Int {
        val n = nums.size
        val size = n / k
        val full = (1 shl n) - 1
        val groups = HashMap<Int, Int>()
        for (mask in 0 until (1 shl n)) {
            if (Integer.bitCount(mask) != size) continue
            val vals = mutableListOf<Int>()
            for (i in 0 until n) if ((mask shr i) and 1 == 1) vals.add(nums[i])
            if (vals.toSet().size == size) {
                groups[mask] = vals.maxOrNull()!! - vals.minOrNull()!!
            }
        }
        val memo = IntArray(1 shl n) { -2 }
        fun dp(mask: Int): Int {
            if (mask == full) return 0
            if (memo[mask] != -2) return memo[mask]
            var first = 0
            while ((mask shr first) and 1 == 1) first++
            var best = 1_000_000_000
            for ((g, c) in groups) {
                if (((g shr first) and 1) == 1 && g and mask == 0) {
                    val sub = dp(mask or g)
                    if (sub < 1_000_000_000) best = minOf(best, c + sub)
                }
            }
            memo[mask] = best
            return best
        }
        val ans = dp(0)
        return if (ans >= 1_000_000_000) -1 else ans
    }
}
