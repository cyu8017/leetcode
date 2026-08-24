// LeetCode 0959 - Regions Cut By Slashes
// https://leetcode.com/problems/regions-cut-by-slashes/

class Solution {
    func regionsBySlashes(_ grid: [String]) -> Int {
        let n = grid.count
        var parent = Array(0..<(n * n * 4))
        func find(_ x: Int) -> Int {
            if parent[x] != x { parent[x] = find(parent[x]) }
            return parent[x]
        }
        func unite(_ a: Int, _ b: Int) { parent[find(a)] = find(b) }
        let rows = grid.map { Array($0) }
        for r in 0..<n {
            for c in 0..<n {
                let root = 4 * (r * n + c)
                let ch = rows[r][c]
                if ch == "/" {
                    unite(root + 0, root + 3)
                    unite(root + 1, root + 2)
                } else if ch == "\\" {
                    unite(root + 0, root + 1)
                    unite(root + 2, root + 3)
                } else {
                    unite(root + 0, root + 1)
                    unite(root + 1, root + 2)
                    unite(root + 2, root + 3)
                }
                if r + 1 < n { unite(root + 2, root + 4 * n + 0) }
                if c + 1 < n { unite(root + 1, root + 4 + 3) }
            }
        }
        var ans = 0
        for i in 0..<parent.count where find(i) == i { ans += 1 }
        return ans
    }
}
