// LeetCode 1697 - Checking Existence of Edge Length Limited Paths
// https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution {
    func distanceLimitedPathsExist(_ n: Int, _ edgeList: [[Int]], _ queries: [[Int]]) -> [Bool] {
        var parent = Array(0..<n)
        func find(_ x: Int) -> Int {
            var x = x
            while x != parent[x] {
                parent[x] = parent[parent[x]]
                x = parent[x]
            }
            return x
        }
        var ans = Array(repeating: false, count: queries.count)
        let edges = edgeList.sorted { $0[2] < $1[2] }
        let qs = queries.enumerated().map { ($0.element[2], $0.element[0], $0.element[1], $0.offset) }
            .sorted { $0.0 < $1.0 }
        var i = 0
        for (limit, p, q, idx) in qs {
            while i < edges.count && edges[i][2] < limit {
                let a = edges[i][0], b = edges[i][1]
                parent[find(a)] = find(b)
                i += 1
            }
            ans[idx] = find(p) == find(q)
        }
        return ans
    }
}
