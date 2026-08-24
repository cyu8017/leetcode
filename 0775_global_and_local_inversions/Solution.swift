// LeetCode 0775 - Global and Local Inversions
// https://leetcode.com/problems/global-and-local-inversions/

class Solution {
    func isIdealPermutation(_ nums: [Int]) -> Bool {
        for i in 0..<nums.count {
            if abs(nums[i] - i) > 1 { return false }
        }
        return true
    }
}
