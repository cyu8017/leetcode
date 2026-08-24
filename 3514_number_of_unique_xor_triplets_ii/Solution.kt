// LeetCode 3514 - Number of Unique XOR Triplets II
// https://leetcode.com/problems/number-of-unique-xor-triplets-ii/

class Solution {
    fun uniqueXorTriplets(nums: IntArray): Int {
        var mx = 0
        for (v in nums) mx = maxOf(mx, v)
        mx = mx shl 1
        val st = BooleanArray(mx)
        for (a in nums) for (b in nums) st[a xor b] = true
        val s = IntArray(mx)
        for (ab in 0 until mx) {
            if (st[ab]) for (c in nums) s[ab xor c] = 1
        }
        var ans = 0
        for (v in s) ans += v
        return ans
    }
}
