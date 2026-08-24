// LeetCode 3978 - Unique Middle Element
// https://leetcode.com/problems/unique-middle-element/


class Solution {
    func isMiddleElementUnique(_ nums: [Int]) -> Bool {
        let mid = nums[nums.count / 2]
        var cnt = 0
        for x in nums { if x == mid { cnt += 1 } }
        return cnt == 1
    }
}
