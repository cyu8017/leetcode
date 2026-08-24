// LeetCode 3684 - Maximize Sum of At Most K Distinct Elements
// https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/

class Solution {
    func maxKDistinct(_ nums: [Int], _ k0: Int) -> [Int] {
        var k = k0
        let nums = nums.sorted()
        var ans = [Int]()
        for i in stride(from: nums.count - 1, through: 0, by: -1) {
            if i + 1 < nums.count && nums[i] == nums[i + 1] { continue }
            ans.append(nums[i])
            k -= 1
            if k == 0 { break }
        }
        return ans
    }
}
