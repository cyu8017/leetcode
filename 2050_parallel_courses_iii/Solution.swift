// LeetCode 2050 - Parallel Courses III
// https://leetcode.com/problems/parallel-courses-iii/

class Solution {
    func minimumTime(_ n: Int, _ relations: [[Int]], _ time: [Int]) -> Int {
        var g = [[Int]](repeating: [], count: n + 1)
        var indeg = [Int](repeating: 0, count: n + 1)
        var dist = [Int](repeating: 0, count: n + 1)
        for e in relations {
            g[e[0]].append(e[1])
            indeg[e[1]] += 1
        }
        var q = [Int]()
        for i in 1...n {
            dist[i] = time[i - 1]
            if indeg[i] == 0 { q.append(i) }
        }
        var head = 0
        while head < q.count {
            let u = q[head]
            head += 1
            for v in g[u] {
                dist[v] = max(dist[v], dist[u] + time[v - 1])
                indeg[v] -= 1
                if indeg[v] == 0 { q.append(v) }
            }
        }
        return dist.max() ?? 0
    }
}
