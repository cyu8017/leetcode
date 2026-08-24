// LeetCode 2045 - Second Minimum Time to Reach Destination
// https://leetcode.com/problems/second-minimum-time-to-reach-destination/

class Solution {
    func secondMinimum(_ n: Int, _ edges: [[Int]], _ time: Int, _ change: Int) -> Int {
        var g = [[Int]](repeating: [], count: n + 1)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        var dist1 = [Int](repeating: -1, count: n + 1)
        var dist2 = [Int](repeating: -1, count: n + 1)
        var q = [(1, 0)]
        dist1[1] = 0
        var head = 0
        while head < q.count {
            let (u, d) = q[head]
            head += 1
            for v in g[u] {
                let nd = d + 1
                if dist1[v] == -1 {
                    dist1[v] = nd
                    q.append((v, nd))
                } else if dist2[v] == -1 && nd > dist1[v] {
                    dist2[v] = nd
                    q.append((v, nd))
                }
            }
        }
        let steps = dist2[n]
        var ans = 0
        for _ in 0..<steps {
            if (ans / change) % 2 == 1 { ans += change - ans % change }
            ans += time
        }
        return ans
    }
}
