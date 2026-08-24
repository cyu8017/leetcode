// LeetCode 3674 - Minimum Operations to Equalize Array
// https://leetcode.com/problems/minimum-operations-to-equalize-array/

class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        for x in nums where x != nums[0] { return 1 }
        return 0
    }
}
