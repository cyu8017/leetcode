// LeetCode 3560 - Find Minimum Log Transportation Cost
// https://leetcode.com/problems/find-minimum-log-transportation-cost/

class Solution {
    func minCuttingCost(_ n: Int, _ m: Int, _ k: Int) -> Int {
        let x = max(n, m)
        if x <= k { return 0 }
        return k * (x - k)
    }
}
