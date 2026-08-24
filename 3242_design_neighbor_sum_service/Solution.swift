// LeetCode 3242 - Design Neighbor Sum Service
// https://leetcode.com/problems/design-neighbor-sum-service/

class NeighborSum {
    private let grid: [[Int]]
    private var d: [Int: (Int, Int)] = [:]
    private let dirs = [[-1, 0, 1, 0, -1], [-1, 1, 1, -1, -1]]

    init(_ grid: [[Int]]) {
        self.grid = grid
        for i in 0..<grid.count {
            for j in 0..<grid[i].count {
                d[grid[i][j]] = (i, j)
            }
        }
    }

    func adjacentSum(_ value: Int) -> Int { cal(value, 0) }
    func diagonalSum(_ value: Int) -> Int { cal(value, 1) }

    private func cal(_ value: Int, _ k: Int) -> Int {
        guard let p = d[value] else { return 0 }
        var s = 0
        for q in 0..<4 {
            let x = p.0 + dirs[k][q], y = p.1 + dirs[k][q + 1]
            if x >= 0 && x < grid.count && y >= 0 && y < grid[0].count {
                s += grid[x][y]
            }
        }
        return s
    }
}
