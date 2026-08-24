// LeetCode 0698 - Partition to K Equal Sum Subsets
// https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution {
    func canPartitionKSubsets(_ nums: [Int], _ k: Int) -> Bool {
        let total = nums.reduce(0, +)
        if total % k != 0 { return false }
        let target = total / k
        var nums = nums.sorted(by: >)
        if nums[0] > target { return false }
        var buckets = Array(repeating: 0, count: k)
        func dfs(_ index: Int) -> Bool {
            if index == nums.count { return true }
            for i in 0..<buckets.count {
                if buckets[i] + nums[index] > target { continue }
                buckets[i] += nums[index]
                if dfs(index + 1) { return true }
                buckets[i] -= nums[index]
                if buckets[i] == 0 { break }
            }
            return false
        }
        return dfs(0)
    }
}
