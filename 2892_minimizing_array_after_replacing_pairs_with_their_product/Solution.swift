// LeetCode 2892 - Minimizing Array After Replacing Pairs With Their Product
// https://leetcode.com/problems/minimizing-array-after-replacing-pairs-with-their-product/

class Solution {
    func minArrayLength(_ nums: [Int], _ k: Int) -> Int {
        if nums.isEmpty { return 0 }
        var ans = 1
        var prod = nums[0]
        for i in 1..<nums.count {
            if prod <= k && nums[i] <= k && (nums[i] == 0 || prod <= k / nums[i]) {
                prod *= nums[i]
            } else {
                ans += 1
                prod = nums[i]
            }
        }
        return ans
    }
}
