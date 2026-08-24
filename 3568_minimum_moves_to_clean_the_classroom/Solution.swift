// LeetCode 3568 - Minimum Moves to Clean the Classroom
// https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/

class Solution {
    func minMoves(_ classroom: [String], _ energy: Int) -> Int {
        let m = classroom.count
        let grid = classroom.map { Array($0) }
        let n = grid[0].count
        var d = Array(repeating: Array(repeating: 0, count: n), count: m)
        var x = 0, y = 0, cnt = 0
        for i in 0..<m {
            for j in 0..<n {
                let c = grid[i][j]
                if c == "S" { x = i; y = j }
                else if c == "L" { d[i][j] = cnt; cnt += 1 }
            }
        }
        if cnt == 0 { return 0 }
        var vis = Array(repeating: Array(repeating: Array(repeating: Array(repeating: false, count: 1 << cnt), count: energy + 1), count: n), count: m)
        var q = [[x, y, energy, (1 << cnt) - 1]]
        vis[x][y][energy][(1 << cnt) - 1] = true
        let dirs = [-1, 0, 1, 0, -1]
        var ans = 0
        while !q.isEmpty {
            let t = q
            q = []
            for s in t {
                let i = s[0], j = s[1], curEnergy = s[2], mask = s[3]
                if mask == 0 { return ans }
                if curEnergy <= 0 { continue }
                for k in 0..<4 {
                    let nx = i + dirs[k], ny = j + dirs[k + 1]
                    if nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] != "X" {
                        let nxtEnergy = grid[nx][ny] == "R" ? energy : curEnergy - 1
                        var nxtMask = mask
                        if grid[nx][ny] == "L" { nxtMask &= ~(1 << d[nx][ny]) }
                        if !vis[nx][ny][nxtEnergy][nxtMask] {
                            vis[nx][ny][nxtEnergy][nxtMask] = true
                            q.append([nx, ny, nxtEnergy, nxtMask])
                        }
                    }
                }
            }
            ans += 1
        }
        return -1
    }
}
