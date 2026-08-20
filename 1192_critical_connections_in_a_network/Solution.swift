// LeetCode 1192 - Critical Connections in a Network
// https://leetcode.com/problems/critical-connections-in-a-network/

class Solution {
    func criticalConnections(_ n: Int, _ connections: [[Int]]) -> [[Int]] {
        var graph = [[Int]](repeating: [], count: n)
        for e in connections {
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        }
        var disc = [Int](repeating: -1, count: n)
        var low = [Int](repeating: 0, count: n)
        var time = 0
        var ans: [[Int]] = []
        func dfs(_ u: Int, _ parent: Int) {
            disc[u] = time
            low[u] = time
            time += 1
            for v in graph[u] where v != parent {
                if disc[v] == -1 {
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u] { ans.append([u, v]) }
                } else {
                    low[u] = min(low[u], disc[v])
                }
            }
        }
        for i in 0..<n where disc[i] == -1 { dfs(i, -1) }
        return ans
    }
}
