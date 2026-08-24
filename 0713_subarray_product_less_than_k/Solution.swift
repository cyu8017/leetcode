// LeetCode 0713 - Subarray Product Less Than K
// https://leetcode.com/problems/subarray-product-less-than-k/

class Solution {
    func numSubarrayProductLessThanK(_ nums: [Int], _ k: Int) -> Int {
        if k <= 1 { return 0 }
        var prod = 1, left = 0, ans = 0
        for right in 0..<nums.count {
            prod *= nums[right]
            while prod >= k {
                prod /= nums[left]
                left += 1
            }
            ans += right - left + 1
        }
        return ans
    }
}
