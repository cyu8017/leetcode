// LeetCode 1284 - Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
// https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/

class Solution {
    func minFlips(_ mat: [[Int]]) -> Int {
        let m = mat.count, n = mat[0].count
        var start = 0
        for i in 0..<m {
            for j in 0..<n where mat[i][j] == 1 {
                start |= 1 << (i * n + j)
            }
        }
        if start == 0 { return 0 }
        var q = [(start, 0)]
        var seen = Set<Int>([start])
        var qi = 0
        let dirs = [(0,0),(1,0),(-1,0),(0,1),(0,-1)]
        while qi < q.count {
            let (state, dist) = q[qi]; qi += 1
            for i in 0..<m {
                for j in 0..<n {
                    var next = state
                    for (dr, dc) in dirs {
                        let nr = i + dr, nc = j + dc
                        if nr >= 0 && nr < m && nc >= 0 && nc < n {
                            next ^= 1 << (nr * n + nc)
                        }
                    }
                    if next == 0 { return dist + 1 }
                    if !seen.contains(next) {
                        seen.insert(next)
                        q.append((next, dist + 1))
                    }
                }
            }
        }
        return -1
    }
}
