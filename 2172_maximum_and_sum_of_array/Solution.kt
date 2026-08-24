// LeetCode 2172 - Maximum AND Sum of Array
// https://leetcode.com/problems/maximum-and-sum-of-array/

class Solution {
    fun maximumANDSum(nums: IntArray, numSlots: Int): Int {
        var n: Int = nums.size, slots = numSlots, maxMask = 1
        for (i in 0 until slots) maxMask *= 3
        var dp: IntArray = IntArray(maxMask)
        for (mask in 0 until maxMask) {
            var cnt: Int = 0, x = mask
            while (x > 0) { cnt += x % 3; x /= 3; }
            if (cnt >= n) continue
            var v: Int = nums[cnt], bas = 1
            for (s in 1 until = slots) {
                var occ: Int = (mask / bas) % 3
                if (occ < 2) {
                    var nm: Int = mask + bas
                    dp[nm] = maxOf(dp[nm], dp[mask] + (v & s))
                }
                bas *= 3
            }
        }
        var best: Int = 0
        for (v in dp) best = maxOf(best, v)
        return best
    }
}
