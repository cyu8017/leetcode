// LeetCode 0487 - Max Consecutive Ones II
// https://leetcode.com/problems/max-consecutive-ones-ii/

class Solution {
    func findMaxConsecutiveOnes(_ nums: [Int]) -> Int {
        var left = 0
        var best = 0
        var zeros = 0
        for right in 0..<nums.count {
            if nums[right] == 0 {
                zeros += 1
            }
            while zeros > 1 {
                if nums[left] == 0 {
                    zeros -= 1
                }
                left += 1
            }
            best = max(best, right - left + 1)
        }
        return best
    }
}
