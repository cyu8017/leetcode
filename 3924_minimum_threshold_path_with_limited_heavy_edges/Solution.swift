// LeetCode 3924 - Minimum Threshold Path With Limited Heavy Edges
// https://leetcode.com/problems/minimum-threshold-path-with-limited-heavy-edges/


class Solution {
    func minThreshold(_ n: Int, _ edges: [[Int]], _ source: Int, _ target: Int, _ k: Int) -> Int {
        if source == target { return 0 }
        var g = Array(repeating: [(Int, Int)](), count: n)
        var maxWeight = 0
        for e in edges {
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))
            maxWeight = max(maxWeight, e[2])
        }
        func can(_ threshold: Int) -> Bool {
            let inf = 1_000_000_000
            var dist = Array(repeating: inf, count: n)
            dist[source] = 0
            var dq = [source]
            var head = 0
            while head < dq.count {
                let u = dq[head]; head += 1
                for (to, weight) in g[u] {
                    let cost = weight > threshold ? 1 : 0
                    if dist[u] + cost >= dist[to] || dist[u] + cost > k { continue }
                    dist[to] = dist[u] + cost
                    if cost == 0 {
                        dq.insert(to, at: head)
                    } else {
                        dq.append(to)
                    }
                }
            }
            return dist[target] <= k
        }
        if !can(maxWeight) { return -1 }
        var lo = 0, hi = maxWeight
        while lo < hi {
            let mid = lo + (hi - lo) / 2
            if can(mid) { hi = mid }
            else { lo = mid + 1 }
        }
        return lo
    }
}
