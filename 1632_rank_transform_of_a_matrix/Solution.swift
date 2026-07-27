// LeetCode 1632 - Rank Transform of a Matrix
// https://leetcode.com/problems/rank-transform-of-a-matrix/

class Solution {
    func matrixRankTransform(_ matrix: [[Int]]) -> [[Int]] {
        let m = matrix.count, n = matrix[0].count
        var groups = [Int: [(Int, Int)]]()
        for i in 0..<m {
            for j in 0..<n {
                groups[matrix[i][j], default: []].append((i, j))
            }
        }
        var rank = [Int](repeating: 0, count: m + n)
        var ans = [[Int]](repeating: [Int](repeating: 0, count: n), count: m)
        for value in groups.keys.sorted() {
            var parent = [Int: Int]()
            func find(_ x: Int) -> Int {
                if parent[x] == nil { parent[x] = x }
                if parent[x]! != x {
                    parent[x] = find(parent[x]!)
                }
                return parent[x]!
            }
            for (i, j) in groups[value]! {
                let a = find(i), b = find(m + j)
                parent[a] = b
            }
            var best = [Int: Int]()
            for (i, j) in groups[value]! {
                let root = find(i)
                best[root] = max(best[root, default: 0], max(rank[i], rank[m + j]))
            }
            for (i, j) in groups[value]! {
                let r = best[find(i)]! + 1
                ans[i][j] = r
            }
            for (i, j) in groups[value]! {
                rank[i] = max(rank[i], ans[i][j])
                rank[m + j] = max(rank[m + j], ans[i][j])
            }
        }
        return ans
    }
}
