// LeetCode 3585 - Find Weighted Median Node in Tree
// https://leetcode.com/problems/find-weighted-median-node-in-tree/

class Solution {
    func findMedian(_ n: Int, _ edges: [[Int]], _ queries: [[Int]]) -> [Int] {
        var g = Array(repeating: [[Int]](), count: n)
        for e in edges {
            g[e[0]].append([e[1], e[2]])
            g[e[1]].append([e[0], e[2]])
        }
        var ans = Array(repeating: 0, count: queries.count)
        for qi in 0..<queries.count {
            let u = queries[qi][0], v = queries[qi][1]
            var parent = Array(repeating: -2, count: n)
            var pw = Array(repeating: 0, count: n)
            parent[u] = -1
            var q = [u]
            var head = 0
            while head < q.count {
                let x = q[head]; head += 1
                if x == v { break }
                for e in g[x] {
                    if parent[e[0]] == -2 {
                        parent[e[0]] = x
                        pw[e[0]] = e[1]
                        q.append(e[0])
                    }
                }
            }
            var nodes = [v]
            var weights = [Int]()
            var cur = v
            while cur != u {
                weights.append(pw[cur])
                cur = parent[cur]
                nodes.append(cur)
            }
            nodes.reverse()
            weights.reverse()
            var total = 0
            for w in weights { total += w }
            let need = (total + 1) / 2
            var sum = 0, med = u
            for i in 0..<weights.count {
                sum += weights[i]
                med = nodes[i + 1]
                if sum >= need { break }
            }
            ans[qi] = med
        }
        return ans
    }
}
