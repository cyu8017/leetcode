// LeetCode 0164 - Maximum Gap
// https://leetcode.com/problems/maximum-gap/

class Solution {
    func maximumGap(_ nums: [Int]) -> Int {
        guard nums.count >= 2, let low = nums.min(), let high = nums.max(), low != high else { return 0 }
        let bucketSize = max(1, (high - low) / (nums.count - 1))
        let bucketCount = (high - low) / bucketSize + 1
        var mins = Array(repeating: Int.max, count: bucketCount)
        var maxs = Array(repeating: Int.min, count: bucketCount)
        var used = Array(repeating: false, count: bucketCount)
        for number in nums {
            let index = (number - low) / bucketSize
            used[index] = true
            mins[index] = min(mins[index], number)
            maxs[index] = max(maxs[index], number)
        }
        var best = 0, previousMax = low
        for index in 0..<bucketCount where used[index] {
            best = max(best, mins[index] - previousMax)
            previousMax = maxs[index]
        }
        return best
    }
}