// LeetCode 0361 - Bomb Enemy
// https://leetcode.com/problems/bomb-enemy/

class Solution {
    func maxKilledEnemies(_ grid: [[String]]) -> Int {
        if grid.isEmpty || grid[0].isEmpty {
            return 0
        }

        let rows = grid.count
        let cols = grid[0].count
        var rowHits = Array(repeating: Array(repeating: 0, count: cols), count: rows)
        var colHits = Array(repeating: Array(repeating: 0, count: cols), count: rows)

        for row in 0..<rows {
            var count = 0
            for col in 0..<cols {
                if grid[row][col] == "W" {
                    count = 0
                } else if grid[row][col] == "E" {
                    count += 1
                } else {
                    rowHits[row][col] = count
                }
            }

            count = 0
            for col in stride(from: cols - 1, through: 0, by: -1) {
                if grid[row][col] == "W" {
                    count = 0
                } else if grid[row][col] == "E" {
                    count += 1
                } else {
                    rowHits[row][col] += count
                }
            }
        }

        for col in 0..<cols {
            var count = 0
            for row in 0..<rows {
                if grid[row][col] == "W" {
                    count = 0
                } else if grid[row][col] == "E" {
                    count += 1
                } else {
                    colHits[row][col] = count
                }
            }

            count = 0
            for row in stride(from: rows - 1, through: 0, by: -1) {
                if grid[row][col] == "W" {
                    count = 0
                } else if grid[row][col] == "E" {
                    count += 1
                } else {
                    colHits[row][col] += count
                }
            }
        }

        var best = 0
        for row in 0..<rows {
            for col in 0..<cols {
                best = max(best, rowHits[row][col] + colHits[row][col])
            }
        }

        return best
    }
}
