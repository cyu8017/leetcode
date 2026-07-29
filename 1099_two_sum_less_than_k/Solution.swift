// LeetCode 1099 - Two Sum Less Than K
// https://leetcode.com/problems/two-sum-less-than-k/

class Solution {
    func twoSumLessThanK(_ nums: [Int], _ k: Int) -> Int {
        var nums = nums.sorted()
        var lo = 0
        var hi = nums.count - 1
        var ans = -1
        while lo < hi {
            let total = nums[lo] + nums[hi]
            if total < k {
                ans = max(ans, total)
                lo += 1
            } else {
                hi -= 1
            }
        }
        return ans
    }
}
