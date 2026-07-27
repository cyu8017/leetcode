// LeetCode 1658 - Minimum Operations to Reduce X to Zero
// https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

class Solution {
    func minOperations(_ nums: [Int], _ x: Int) -> Int {
        let target = nums.reduce(0, +) - x
        if target < 0 { return -1 }
        var best = -1, left = 0, cur = 0
        for right in 0..<nums.count {
            cur += nums[right]
            while cur > target {
                cur -= nums[left]
                left += 1
            }
            if cur == target {
                best = max(best, right - left + 1)
            }
        }
        return best < 0 ? -1 : nums.count - best
    }
}
