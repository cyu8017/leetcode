// LeetCode 2357 - Make Array Zero by Subtracting Equal Amounts
// https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

class Solution {
    func minimumOperations(_ nums: [Int]) -> Int {
        Set(nums.filter { $0 > 0 }).count
    }
}
