// LeetCode 3512 - Minimum Operations to Make Array Sum Divisible by K
// https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/

class Solution {
    func minOperations(_ nums: [Int], _ k: Int) -> Int {
        var ans = 0
        for x in nums { ans = (ans + x) % k }
        return ans
    }
}
