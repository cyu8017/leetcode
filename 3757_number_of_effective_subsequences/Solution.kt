// LeetCode 3757 - Number of Effective Subsequences
// https://leetcode.com/problems/number-of-effective-subsequences/

class Solution {
    private fun popCount(x0: Int): Int {
        var x = x0
        var c = 0
        while (x != 0) {
            c += x and 1
            x = x shr 1
        }
        return c
    }

    fun countEffectiveSubsequences(nums: IntArray): Int {
        val mod = 1000000007
        var all = 0
        for (x in nums) all = all or x
        val bits = ArrayList<Int>()
        for (b in 0 until 20) {
            if (((all shr b) and 1) != 0) bits.add(b)
        }
        val m = bits.size
        val freq = IntArray(1 shl m)
        for (x in nums) {
            var mask = 0
            for (i in 0 until m) {
                if (((x shr bits[i]) and 1) != 0) mask = mask or (1 shl i)
            }
            freq[mask]++
        }
        val disjoint = freq.copyOf()
        for (b in 0 until m) {
            for (mask in 0 until (1 shl m)) {
                if (((mask shr b) and 1) != 0) {
                    disjoint[mask] += disjoint[mask xor (1 shl b)]
                }
            }
        }
        val pow2 = IntArray(nums.size + 1)
        pow2[0] = 1
        for (i in 1..nums.size) pow2[i] = pow2[i - 1] * 2 % mod
        var ans = 0
        val full = (1 shl m) - 1
        for (s in 1..full) {
            val ways = pow2[disjoint[full xor s]]
            val bc = popCount(s)
            if ((bc and 1) != 0) {
                ans += ways
                if (ans >= mod) ans -= mod
            } else {
                ans -= ways
                if (ans < 0) ans += mod
            }
        }
        return ans
    }
}
