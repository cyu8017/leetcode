// LeetCode 0454 - 4Sum II
// https://leetcode.com/problems/4sum-ii/

class Solution {
    fun fourSumCount(nums1: IntArray, nums2: IntArray, nums3: IntArray, nums4: IntArray): Int {
        val pairSums = HashMap<Int, Int>()
        for (a in nums1) {
            for (b in nums2) {
                val sum = a + b
                pairSums[sum] = pairSums.getOrDefault(sum, 0) + 1
            }
        }
        var total = 0
        for (c in nums3) {
            for (d in nums4) {
                total += pairSums.getOrDefault(-(c + d), 0)
            }
        }
        return total
    }
}
