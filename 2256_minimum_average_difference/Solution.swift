// LeetCode 2256 - Minimum Average Difference
// https://leetcode.com/problems/minimum-average-difference/

class Solution {
    func minimumAverageDifference(_ nums: [Int]) -> Int {
        let n = nums.count
        let total = nums.reduce(0, +)
        var left = 0, bestDiff = Int.max, bestIdx = 0
        for i in 0..<n {
            left += nums[i]
            let leftAvg = left / (i + 1)
            let rightAvg = i != n - 1 ? (total - left) / (n - i - 1) : 0
            let diff = abs(leftAvg - rightAvg)
            if diff < bestDiff {
                bestDiff = diff
                bestIdx = i
            }
        }
        return bestIdx
    }
}
