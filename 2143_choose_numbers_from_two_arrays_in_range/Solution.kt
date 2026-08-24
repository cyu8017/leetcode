// LeetCode 2143 - Choose Numbers From Two Arrays in Range
// https://leetcode.com/problems/choose-numbers-from-two-arrays-in-range/

class Solution {
    fun countSubranges(nums1: IntArray, nums2: IntArray): Int {
        val mod = 1_000_000_007
        val n = nums1.size
        var ans = 0
        var dp = HashMap<Int, Int>()
        for (i in 0 until n) {
            val ndp = HashMap<Int, Int>()
            ndp[nums1[i]] = (ndp.getOrDefault(nums1[i], 0) + 1) % mod
            ndp[-nums2[i]] = (ndp.getOrDefault(-nums2[i], 0) + 1) % mod
            for ((diff, cnt) in dp) {
                ndp[diff + nums1[i]] = (ndp.getOrDefault(diff + nums1[i], 0) + cnt) % mod
                ndp[diff - nums2[i]] = (ndp.getOrDefault(diff - nums2[i], 0) + cnt) % mod
            }
            dp = ndp
            ans = (ans + dp.getOrDefault(0, 0)) % mod
        }
        return ans
    }
}
