// LeetCode 3584 - Maximum Product of First and Last Elements of a Subsequence
// https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence/

class Solution {
    func maximumProduct(_ nums: [Int], _ m: Int) -> Int {
        var ans = Int.min
        var mx = Int.min, mi = Int.max
        for i in (m - 1)..<nums.count {
            let x = nums[i], y = nums[i - m + 1]
            mi = min(mi, y)
            mx = max(mx, y)
            ans = max(ans, max(x * mi, x * mx))
        }
        return ans
    }
}
