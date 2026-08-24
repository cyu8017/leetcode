// LeetCode 3392 - Count Subarrays of Length Three With a Condition
// https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/

class Solution {
    func countSubarrays(_ nums: [Int]) -> Int {
        var ans = 0
        if nums.count >= 3 {
            for i in 0..<(nums.count - 2) {
                if nums[i] * 2 + nums[i + 2] * 2 == nums[i + 1] { ans += 1 }
            }
        }
        return ans
    }
}
