// LeetCode 0864 - Shortest Path to Get All Keys
// https://leetcode.com/problems/shortest-path-to-get-all-keys/

class Solution {
    func shortestPathAllKeys(_ grid: [String]) -> Int {
        let cells = grid.map { Array($0) }
        let m = cells.count, n = cells[0].count
        var allKeys = 0, sr = 0, sc = 0
        for i in 0..<m {
            for j in 0..<n {
                let ch = cells[i][j]
                if ch == "@" { sr = i; sc = j }
                else if ch >= "a" && ch <= "f" {
                    allKeys |= 1 << (Int(ch.asciiValue!) - Int(Character("a").asciiValue!))
                }
            }
        }
        var queue = [(sr, sc, 0, 0)]
        var seen: Set<Int> = [encode(sr, sc, 0)]
        let dr = [1, -1, 0, 0], dc = [0, 0, 1, -1]
        var qi = 0
        while qi < queue.count {
            let (r, c, mask, dist) = queue[qi]
            qi += 1
            if mask == allKeys { return dist }
            for k in 0..<4 {
                let nr = r + dr[k], nc = c + dc[k]
                if nr < 0 || nr >= m || nc < 0 || nc >= n || cells[nr][nc] == "#" { continue }
                let cell = cells[nr][nc]
                var nmask = mask
                if cell >= "a" && cell <= "f" {
                    nmask |= 1 << (Int(cell.asciiValue!) - Int(Character("a").asciiValue!))
                }
                if cell >= "A" && cell <= "F" {
                    let bit = 1 << (Int(cell.asciiValue!) - Int(Character("A").asciiValue!))
                    if mask & bit == 0 { continue }
                }
                let key = encode(nr, nc, nmask)
                if seen.insert(key).inserted {
                    queue.append((nr, nc, nmask, dist + 1))
                }
            }
        }
        return -1
    }

    private func encode(_ r: Int, _ c: Int, _ mask: Int) -> Int {
        return (r << 20) | (c << 10) | mask
    }
}
