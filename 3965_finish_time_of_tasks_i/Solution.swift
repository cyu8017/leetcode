// LeetCode 3965 - Finish Time of Tasks I
// https://leetcode.com/problems/finish-time-of-tasks-i/


class Solution {
    func finishTime(_ n: Int, _ edges: [[Int]], _ baseTime: [Int]) -> Int {
        var g = Array(repeating: [Int](), count: n)
        for e in edges { g[e[0]].append(e[1]) }
        func dfs(_ i: Int) -> Int {
            if g[i].isEmpty { return baseTime[i] }
            let INF = Int.max / 4
            var earliest = INF, latest = -INF
            for j in g[i] {
                let a = dfs(j)
                earliest = min(earliest, a)
                latest = max(latest, a)
            }
            let ownDuration = (latest - earliest) + baseTime[i]
            return latest + ownDuration
        }
        return dfs(0)
    }
}
