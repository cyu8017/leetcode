// LeetCode 2959 - Number of Possible Sets of Closing Branches
// https://leetcode.com/problems/number-of-possible-sets-of-closing-branches/

class Solution {
    func numberOfSets(_ n: Int, _ maxDistance: Int, _ roads: [[Int]]) -> Int {
        var ans = 0
        for mask in 0..<(1 << n) {
            var dist = Array(repeating: Array(repeating: 1 << 29, count: n), count: n)
            for i in 0..<n { dist[i][i] = 0 }
            for r in roads {
                let u = r[0], v = r[1], w = r[2]
                if (mask & (1 << u)) != 0 && (mask & (1 << v)) != 0 && w < dist[u][v] {
                    dist[u][v] = w
                    dist[v][u] = w
                }
            }
            for k in 0..<n where (mask & (1 << k)) != 0 {
                for i in 0..<n where (mask & (1 << i)) != 0 {
                    for j in 0..<n where (mask & (1 << j)) != 0 {
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                    }
                }
            }
            var ok = true
            for i in 0..<n where (mask & (1 << i)) != 0 {
                for j in 0..<n where (mask & (1 << j)) != 0 {
                    if dist[i][j] > maxDistance {
                        ok = false
                        break
                    }
                }
                if !ok { break }
            }
            if ok { ans += 1 }
        }
        return ans
    }
}
