// LeetCode 3282 - Reach End of Array With Max Score
// https://leetcode.com/problems/reach-end-of-array-with-max-score/

class Solution {
    func findMaximumScore(_ nums: [Int]) -> Int {
        var ans = 0, maxV = 0
        for i in 0..<(nums.count - 1) {
            maxV = max(maxV, nums[i])
            ans += maxV
        }
        return ans
    }
}
