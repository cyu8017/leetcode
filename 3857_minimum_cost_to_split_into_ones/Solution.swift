// LeetCode 3857 - Minimum Cost To Split Into Ones
// https://leetcode.com/problems/minimum-cost-to-split-into-ones/

class Solution {
    func minCost(_ n: Int) -> Int {
        return n * (n - 1) / 2
    }
}
