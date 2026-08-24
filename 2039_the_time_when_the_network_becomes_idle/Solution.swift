// LeetCode 2039 - The Time When the Network Becomes Idle
// https://leetcode.com/problems/the-time-when-the-network-becomes-idle/

class Solution {
    func networkBecomesIdle(_ edges: [[Int]], _ patience: [Int]) -> Int {
        let n = patience.count
        var g = [[Int]](repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        var dist = [Int](repeating: -1, count: n)
        var q = [0]
        dist[0] = 0
        var head = 0
        while head < q.count {
            let u = q[head]
            head += 1
            for v in g[u] where dist[v] == -1 {
                dist[v] = dist[u] + 1
                q.append(v)
            }
        }
        var ans = 0
        for i in 1..<n {
            let round = dist[i] * 2
            let lastSend = (round - 1) / patience[i] * patience[i]
            ans = max(ans, lastSend + round)
        }
        return ans + 1
    }
}
