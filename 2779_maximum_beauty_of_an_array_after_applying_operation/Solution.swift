// LeetCode 2779 - Maximum Beauty of an Array After Applying Operation
// https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/

class Solution {
    func maximumBeauty(_ nums: [Int], _ k: Int) -> Int {
        let nums = nums.sorted()
        var ans = 0, left = 0
        for right in nums.indices {
            while nums[right] - nums[left] > 2 * k { left += 1 }
            ans = max(ans, right - left + 1)
        }
        return ans
    }
}
