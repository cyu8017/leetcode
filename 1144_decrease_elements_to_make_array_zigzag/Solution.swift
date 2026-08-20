// LeetCode 1144 - Decrease Elements To Make Array Zigzag
// https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/

class Solution {
    func movesToMakeZigzag(_ nums: [Int]) -> Int {
        func cost(_ start: Int) -> Int {
            var ans = 0
            var i = start
            while i < nums.count {
                let left = i > 0 ? nums[i - 1] : Int.max
                let right = i + 1 < nums.count ? nums[i + 1] : Int.max
                ans += max(0, nums[i] - min(left, right) + 1)
                i += 2
            }
            return ans
        }
        return min(cost(0), cost(1))
    }
}
