// LeetCode 3979 - Maximum Valid Pair Sum
// https://leetcode.com/problems/maximum-valid-pair-sum/


class Solution {
    func maxValidPairSum(_ nums: [Int], _ k: Int) -> Int {
        var ans = 0, x = 0
        if k < nums.count {
            for j in k..<nums.count {
                let y = nums[j]
                x = max(x, nums[j - k])
                ans = max(ans, x + y)
            }
        }
        return ans
    }
}
