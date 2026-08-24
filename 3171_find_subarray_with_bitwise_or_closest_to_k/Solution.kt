// LeetCode 3171 - Find Subarray With Bitwise OR Closest to K
// https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/

class Solution {
    fun minimumDifference(nums: IntArray, k: Int): Int {
        var mx = 0
        for (v in nums) { mx = maxOf(mx, v) }
        var m = mx ==if (0) 1 else 32 - leadingZeroCount(mx)
        var cnt = IntArray(m)
        var ans = Int.MAX_VALUE
        var s = 0
        var i = 0
        for (j in 0 until nums.size) {
            var x = nums[j]
            s |= x
            ans = minOf(ans, kotlin.math.abs(s - k))
            for (h in 0 until m) { if (((x  shr  h) & 1) != 0) cnt[h]++ }
            while (i < j && s > k) {
                var y = nums[i]
                for (h in 0 until m) {
                    if (((y  shr  h) & 1) != 0) {
                        if (--cnt[h] == 0) s ^= 1  shl  h
                    }
                }
                ans = minOf(ans, kotlin.math.abs(s - k))
                i++
            }
        }
        return ans
    }

    fun leadingZeroCount(x: Int): Int {
        if (x == 0) return 32
        var n = 0
        for (bit in 31 downTo 0) {
            if (((x  shr  bit) & 1) != 0) break
            n++
        }
        return n
    }
}
