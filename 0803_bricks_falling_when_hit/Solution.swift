// LeetCode 0803 - Bricks Falling When Hit
// https://leetcode.com/problems/bricks-falling-when-hit/

class Solution {
    private var parent = [Int]()
    private var size = [Int]()
    private var n = 0
    private var roof = 0

    func hitBricks(_ grid: [[Int]], _ hits: [[Int]]) -> [Int] {
        let m = grid.count
        n = grid[0].count
        roof = m * n
        parent = Array(0...roof)
        size = Array(repeating: 1, count: roof + 1)
        var status = grid
        for hit in hits { status[hit[0]][hit[1]] = 0 }
        let dr = [-1, 1, 0, 0], dc = [0, 0, -1, 1]
        for r in 0..<m {
            for c in 0..<n {
                if status[r][c] == 0 { continue }
                if r == 0 { unite(idx(r, c), roof) }
                for k in 0..<4 {
                    let nr = r + dr[k], nc = c + dc[k]
                    if nr >= 0 && nr < m && nc >= 0 && nc < n && status[nr][nc] == 1 {
                        unite(idx(r, c), idx(nr, nc))
                    }
                }
            }
        }
        var answer = Array(repeating: 0, count: hits.count)
        for i in stride(from: hits.count - 1, through: 0, by: -1) {
            let r = hits[i][0], c = hits[i][1]
            if grid[r][c] == 0 { continue }
            let prev = size[find(roof)]
            status[r][c] = 1
            if r == 0 { unite(idx(r, c), roof) }
            for k in 0..<4 {
                let nr = r + dr[k], nc = c + dc[k]
                if nr >= 0 && nr < m && nc >= 0 && nc < n && status[nr][nc] == 1 {
                    unite(idx(r, c), idx(nr, nc))
                }
            }
            let curr = size[find(roof)]
            answer[i] = max(0, curr - prev - 1)
        }
        return answer
    }

    private func find(_ x: Int) -> Int {
        var x = x
        while parent[x] != x {
            parent[x] = parent[parent[x]]
            x = parent[x]
        }
        return x
    }

    private func unite(_ a: Int, _ b: Int) {
        let ra = find(a), rb = find(b)
        if ra == rb { return }
        parent[ra] = rb
        size[rb] += size[ra]
    }

    private func idx(_ r: Int, _ c: Int) -> Int { r * n + c }
}
