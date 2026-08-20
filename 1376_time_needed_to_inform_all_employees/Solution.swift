// LeetCode 1376 - Time Needed to Inform All Employees
// https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution {
    func numOfMinutes(_ n: Int, _ headID: Int, _ manager: [Int], _ informTime: [Int]) -> Int {
        var children = Array(repeating: [Int](), count: n)
        for (i, p) in manager.enumerated() where p != -1 { children[p].append(i) }
        func dfs(_ u: Int) -> Int {
            children[u].map { dfs($0) }.max().map { $0 + informTime[u] } ?? informTime[u]
        }
        return dfs(headID)
    }
}
