// LeetCode 3689 - Maximum Total Subarray Value I
// https://leetcode.com/problems/maximum-total-subarray-value-i/

class Solution {
    func maxTotalValue(_ nums: [Int], _ k: Int) -> Int {
        var mn = nums[0], mx = nums[0]
        for x in nums {
            mn = min(mn, x)
            mx = max(mx, x)
        }
        return k * (mx - mn)
    }
}
