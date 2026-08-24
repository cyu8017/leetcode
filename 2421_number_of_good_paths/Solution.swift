// LeetCode 2421 - Number of Good Paths
// https://leetcode.com/problems/number-of-good-paths/

class Solution {
    func numberOfGoodPaths(_ vals: [Int], _ edges: [[Int]]) -> Int {
        let n = vals.count
        var g = [[Int]](repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        var parent = Array(0..<n)
        var size = [Int](repeating: 1, count: n)
        func find(_ x: Int) -> Int {
            if parent[x] != x { parent[x] = find(parent[x]) }
            return parent[x]
        }
        var nodes = Array(0..<n)
        nodes.sort { vals[$0] < vals[$1] }
        var ans = n
        var i = 0
        while i < n {
            var j = i
            while j < n && vals[nodes[j]] == vals[nodes[i]] { j += 1 }
            for k in i..<j {
                let u = nodes[k]
                for v in g[u] where vals[v] <= vals[u] {
                    let ru = find(u), rv = find(v)
                    if ru != rv {
                        parent[ru] = rv
                        size[rv] += size[ru]
                    }
                }
            }
            var freq = [Int: Int]()
            for k in i..<j {
                let r = find(nodes[k])
                freq[r, default: 0] += 1
            }
            for c in freq.values { ans += c * (c - 1) / 2 }
            i = j
        }
        return ans
    }
}
