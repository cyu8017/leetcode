// LeetCode 2733 - Neither Minimum nor Maximum
// https://leetcode.com/problems/neither-minimum-nor-maximum/

class Solution {
    func findNonMinOrMax(_ nums: [Int]) -> Int {
        if nums.count < 3 { return -1 }
        let a = nums[0], b = nums[1], c = nums[2]
        return a + b + c - max(a, max(b, c)) - min(a, min(b, c))
    }
}
