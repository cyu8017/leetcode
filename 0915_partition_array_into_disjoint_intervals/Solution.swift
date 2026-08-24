// LeetCode 0915 - Partition Array into Disjoint Intervals
// https://leetcode.com/problems/partition-array-into-disjoint-intervals/

class Solution {
    func partitionDisjoint(_ nums: [Int]) -> Int {
        let n = nums.count
        var minRight = Array(repeating: 0, count: n)
        minRight[n - 1] = nums[n - 1]
        for i in stride(from: n - 2, through: 0, by: -1) {
            minRight[i] = min(nums[i], minRight[i + 1])
        }
        var maxLeft = nums[0]
        for i in 1..<n {
            if maxLeft <= minRight[i] { return i }
            maxLeft = max(maxLeft, nums[i])
        }
        return n - 1
    }
}
