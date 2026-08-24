// LeetCode 2477 - Minimum Fuel Cost to Report to the Capital
// https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

class Solution {
    func minimumFuelCost(_ roads: [[Int]], _ seats: Int) -> Int {
        let n = roads.count + 1
        var g = [[Int]](repeating: [], count: n)
        for r in roads {
            g[r[0]].append(r[1])
            g[r[1]].append(r[0])
        }
        var ans = 0
        func dfs(_ u: Int, _ p: Int) -> Int {
            var people = 1
            for v in g[u] where v != p { people += dfs(v, u) }
            if u != 0 { ans += (people + seats - 1) / seats }
            return people
        }
        _ = dfs(0, -1)
        return ans
    }
}
