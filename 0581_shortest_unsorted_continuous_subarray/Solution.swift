// LeetCode 0581 - Shortest Unsorted Continuous Subarray
// https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution {
    func findUnsortedSubarray(_ nums: [Int]) -> Int {
        let n = nums.count
        var left = -1
        var right = -2
        var maxSeen = nums[0]
        var minSeen = nums[n - 1]
        for i in 0..<n {
            maxSeen = max(maxSeen, nums[i])
            if nums[i] < maxSeen { right = i }
            let j = n - 1 - i
            minSeen = min(minSeen, nums[j])
            if nums[j] > minSeen { left = j }
        }
        return right - left + 1
    }
}
