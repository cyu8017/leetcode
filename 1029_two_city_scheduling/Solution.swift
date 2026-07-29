// LeetCode 1029 - Two City Scheduling
// https://leetcode.com/problems/two-city-scheduling/

class Solution {
    func twoCitySchedCost(_ costs: [[Int]]) -> Int {
        let costs = costs.sorted { $0[0] - $0[1] < $1[0] - $1[1] }
        let n = costs.count / 2
        var ans = 0
        for i in 0..<n { ans += costs[i][0] }
        for i in n..<costs.count { ans += costs[i][1] }
        return ans
    }
}
