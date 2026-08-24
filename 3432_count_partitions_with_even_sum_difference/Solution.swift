// LeetCode 3432 - Count Partitions with Even Sum Difference
// https://leetcode.com/problems/count-partitions-with-even-sum-difference/

class Solution {
    func countPartitions(_ nums: [Int]) -> Int {
        let total = nums.reduce(0, +)
        var ans = 0, left = 0
        for i in 0..<(nums.count - 1) {
            left += nums[i]
            if (left - (total - left)) % 2 == 0 { ans += 1 }
        }
        return ans
    }
}
