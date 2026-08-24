// LeetCode 3038 - Maximum Number of Operations With the Same Score I
// https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i/

class Solution {
    func maxOperations(_ nums: [Int]) -> Int {
        let s = nums[0] + nums[1]
        let n = nums.count
        var ans = 0
        var i = 0
        while i + 1 < n && nums[i] + nums[i + 1] == s {
            ans += 1
            i += 2
        }
        return ans
    }
}
