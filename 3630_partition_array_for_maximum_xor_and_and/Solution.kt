// LeetCode 3630 - Partition Array for Maximum XOR and AND
// https://leetcode.com/problems/partition-array-for-maximum-xor-and-and/

class Solution {
    fun maximizeXorAndXor(nums: IntArray): Long {
        val n = nums.size
        var best = 0L
        for (mask in 0 until (1 shl n)) {
            var andVal = -1
            var xorRest = 0
            for (i in 0 until n) {
                if (((mask shr i) and 1) != 0) {
                    andVal = if (andVal < 0) nums[i] else (andVal and nums[i])
                } else {
                    xorRest = xorRest xor nums[i]
                }
            }
            if (andVal < 0) andVal = 0
            val comp = ((1 shl n) - 1) xor mask
            var sub = comp
            while (true) {
                var x1 = 0
                for (i in 0 until n) {
                    if (((sub shr i) and 1) != 0) x1 = x1 xor nums[i]
                }
                val x2 = xorRest xor x1
                best = maxOf(best, andVal.toLong() + x1 + x2)
                if (sub == 0) break
                sub = (sub - 1) and comp
            }
        }
        return best
    }
}
