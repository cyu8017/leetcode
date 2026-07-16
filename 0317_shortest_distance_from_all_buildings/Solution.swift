// LeetCode 0317 - Shortest Distance from All Buildings
// https://leetcode.com/problems/shortest-distance-from-all-buildings/

class Solution {
    func shortestDistance(_ grid: [[Int]]) -> Int {
        if grid.isEmpty {
            return -1
        }

        let rows = grid.count
        let cols = grid[0].count
        var buildings = 0
        for row in grid {
            for cell in row where cell == 1 {
                buildings += 1
            }
        }

        var distances = Array(repeating: Array(repeating: 0, count: cols), count: rows)
        var reach = Array(repeating: Array(repeating: 0, count: cols), count: rows)
        let directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for row in 0..<rows {
            for col in 0..<cols {
                if grid[row][col] != 1 {
                    continue
                }
                var queue: [(Int, Int, Int)] = [(row, col, 0)]
                var visited = Set<[Int]>()
                visited.insert([row, col])
                while !queue.isEmpty {
                    let (currentRow, currentCol, distance) = queue.removeFirst()
                    for (dr, dc) in directions {
                        let nr = currentRow + dr
                        let nc = currentCol + dc
                        if nr < 0 || nr >= rows || nc < 0 || nc >= cols {
                            continue
                        }
                        if grid[nr][nc] != 0 {
                            continue
                        }
                        let key = [nr, nc]
                        if visited.contains(key) {
                            continue
                        }
                        visited.insert(key)
                        distances[nr][nc] += distance + 1
                        reach[nr][nc] += 1
                        queue.append((nr, nc, distance + 1))
                    }
                }
            }
        }

        var best = Int.max
        for row in 0..<rows {
            for col in 0..<cols {
                if grid[row][col] == 0 && reach[row][col] == buildings {
                    best = min(best, distances[row][col])
                }
            }
        }
        return best == Int.max ? -1 : best
    }
}
