// LeetCode 3868 - Minimum Cost To Equalize Arrays Using Swaps
// https://leetcode.com/problems/minimum-cost-to-equalize-arrays-using-swaps/

class Solution {
    fun minCost(nums1: IntArray, nums2: IntArray): Int {
        var cnt2 = HashMap<Int, Int>()
        for (x in nums2) { cnt2[x] = cnt2.getOrDefault(x, 0 + 1) }
        var cnt1 = HashMap<Int, Int>()
        for (x in nums1) {
            var c = cnt2.getOrDefault(x, 0)
            if (c > 0) cnt2[x] = c - 1
            else cnt1[x] = cnt1.getOrDefault(x, 0 + 1)
        }
        var ans = 0
        for (v in cnt1.values) {
            if (v % 2 == 1) return -1
            ans += v / 2
        }
        for (v in cnt2.values) {
            if (v % 2 == 1) return -1
        }
        return ans
    }
}
