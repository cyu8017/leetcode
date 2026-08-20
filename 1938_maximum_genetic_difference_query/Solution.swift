// LeetCode 1938 - Maximum Genetic Difference Query
// https://leetcode.com/problems/maximum-genetic-difference-query/

class Solution {
    func maxGeneticDifference(_ parents: [Int], _ queries: [[Int]]) -> [Int] {
        let n = parents.count
        var children = Array(repeating: [Int](), count: n)
        var root = 0
        for (i, p) in parents.enumerated() {
            if p == -1 { root = i }
            else { children[p].append(i) }
        }
        var qmap = Array(repeating: [(Int, Int)](), count: n)
        for (i, q) in queries.enumerated() {
            qmap[q[0]].append((i, q[1]))
        }
        var ans = Array(repeating: 0, count: queries.count)
        let BITS = 17
        var child0 = Array(repeating: -1, count: (n + 2) * (BITS + 2))
        var child1 = Array(repeating: -1, count: (n + 2) * (BITS + 2))
        var cnt = Array(repeating: 0, count: (n + 2) * (BITS + 2))
        var nodes = 1

        func trieUpdate(_ num: Int, _ delta: Int) {
            var node = 0
            for b in stride(from: BITS, through: 0, by: -1) {
                let bit = (num >> b) & 1
                if bit == 0 {
                    if child0[node] == -1 {
                        child0[node] = nodes
                        nodes += 1
                    }
                    node = child0[node]
                } else {
                    if child1[node] == -1 {
                        child1[node] = nodes
                        nodes += 1
                    }
                    node = child1[node]
                }
                cnt[node] += delta
            }
        }
        func trieMaxXor(_ num: Int) -> Int {
            var node = 0, res = 0
            for b in stride(from: BITS, through: 0, by: -1) {
                let bit = (num >> b) & 1
                let want = 1 - bit
                if want == 1, child1[node] != -1, cnt[child1[node]] > 0 {
                    res |= 1 << b
                    node = child1[node]
                } else if want == 0, child0[node] != -1, cnt[child0[node]] > 0 {
                    res |= 1 << b
                    node = child0[node]
                } else if bit == 1 {
                    node = child1[node]
                } else {
                    node = child0[node]
                }
            }
            return res
        }
        func dfs(_ u: Int) {
            trieUpdate(u, 1)
            for (qi, val) in qmap[u] {
                ans[qi] = trieMaxXor(val)
            }
            for v in children[u] { dfs(v) }
            trieUpdate(u, -1)
        }
        dfs(root)
        return ans
    }
}
