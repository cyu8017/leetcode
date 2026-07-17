// LeetCode 1793 - Maximum Score of a Good Subarray
// https://leetcode.com/problems/maximum-score-of-a-good-subarray/

class Solution {
    func maximumScore(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var stack: [Int] = []
        var ans = 0
        for i in 0...n {
            while let top = stack.last, i == n || nums[i] < nums[top] {
                let mid = stack.removeLast()
                let left = stack.isEmpty ? 0 : stack.last! + 1
                let right = i - 1
                if left <= k && k <= right {
                    ans = max(ans, nums[mid] * (right - left + 1))
                }
            }
            stack.append(i)
        }
        return ans
    }
}
