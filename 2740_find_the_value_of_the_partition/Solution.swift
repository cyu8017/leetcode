// LeetCode 2740 - Find the Value of the Partition
// https://leetcode.com/problems/find-the-value-of-the-partition/

class Solution {
    func findValueOfPartition(_ nums: [Int]) -> Int {
        let nums = nums.sorted()
        var ans = Int.max
        for i in 1..<nums.count { ans = min(ans, nums[i] - nums[i - 1]) }
        return ans
    }
}
