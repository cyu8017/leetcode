// LeetCode 3701 - Compute Alternating Sum
// https://leetcode.com/problems/compute-alternating-sum/

class Solution {
    func alternatingSum(_ nums: [Int]) -> Int {
        var ans = 0
        for i in 0..<nums.count {
            if i % 2 == 0 { ans += nums[i] } else { ans -= nums[i] }
        }
        return ans
    }
}
