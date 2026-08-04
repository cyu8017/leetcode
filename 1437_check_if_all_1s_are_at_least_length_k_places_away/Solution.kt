// LeetCode 1437 - Check If All 1's Are at Least Length K Places Away
// https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

class Solution {
    fun kLengthApart(nums: IntArray, k: Int): Boolean {
        var previous = -k - 1
        for (i in nums.indices) {
            if (nums[i] == 1) {
                if (i - previous <= k) return false
                previous = i
            }
        }
        return true
    }
}
