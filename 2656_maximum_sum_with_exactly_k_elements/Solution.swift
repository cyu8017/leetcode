// LeetCode 2656 - Maximum Sum With Exactly K Elements
// https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

class Solution {
    func maximizeSum(_ nums: [Int], _ k: Int) -> Int {
        let mx = nums.max() ?? 0
        return k * mx + k * (k - 1) / 2
    }
}
