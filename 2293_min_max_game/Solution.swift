// LeetCode 2293 - Min Max Game
// https://leetcode.com/problems/min-max-game/

class Solution {
    func minMaxGame(_ nums: [Int]) -> Int {
        var nums = nums
        while nums.count > 1 {
            var next = [Int](repeating: 0, count: nums.count / 2)
            for i in 0..<next.count {
                if i % 2 == 0 { next[i] = min(nums[2 * i], nums[2 * i + 1]) }
                else { next[i] = max(nums[2 * i], nums[2 * i + 1]) }
            }
            nums = next
        }
        return nums[0]
    }
}
