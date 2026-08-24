// LeetCode 3670 - Maximum Product of Two Integers With No Common Bits
// https://leetcode.com/problems/maximum-product-of-two-integers-with-no-common-bits/

class Solution {
    fun maxProduct(nums: IntArray): Long {
        var maxV = 0
        for (v in nums) { if (v > maxV) maxV = v }
        var bitsN = 0
        run {
            var x = maxV
            while (x > 0) {
                bitsN++
                x >>= 1
            }
        }
        if (bitsN == 0) bitsN = 1
        var size = 1  shl  bitsN
        var best = IntArray(size)
        for (v in nums) { if (v > best[v]) best[v] = v }
        for (mask in 0 until size) {
            for (b in 0 until bitsN) {
                if ((mask & (1  shl  b)) != 0) {
                    var sub = mask ^ (1  shl  b)
                    if (best[sub] > best[mask]) best[mask] = best[sub]
                }
            }
        }
        var ans = 0
        for (v in nums) {
            var comp = (size - 1) ^ v
            if (best[comp] > 0) {
                var p = v * best[comp]
                if (p > ans) ans = p
            }
        }
        return ans
    }
}
