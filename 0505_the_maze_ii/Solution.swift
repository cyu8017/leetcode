// LeetCode 0505 - The Maze II
// https://leetcode.com/problems/the-maze-ii/

class Solution {
    func shortestDistance(_ maze: [[Int]], _ start: [Int], _ destination: [Int]) -> Int {
        let rows = maze.count
        let cols = maze[0].count
        let target = (destination[0], destination[1])
        let directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        var best: [String: Int] = [:]
        var heap: [(Int, Int, Int)] = [(0, start[0], start[1])]

        while !heap.isEmpty {
            heap.sort { $0.0 < $1.0 }
            let (dist, row, col) = heap.removeFirst()
            if row == target.0 && col == target.1 {
                return dist
            }
            let key = "\(row),\(col)"
            if best[key, default: Int.max] <= dist {
                continue
            }
            best[key] = dist

            for (dr, dc) in directions {
                var nextRow = row
                var nextCol = col
                var traveled = 0
                while nextRow + dr >= 0 && nextRow + dr < rows &&
                      nextCol + dc >= 0 && nextCol + dc < cols &&
                      maze[nextRow + dr][nextCol + dc] == 0 {
                    nextRow += dr
                    nextCol += dc
                    traveled += 1
                }
                if nextRow == row && nextCol == col {
                    continue
                }
                let newDist = dist + traveled
                let nextKey = "\(nextRow),\(nextCol)"
                if newDist < best[nextKey, default: Int.max] {
                    heap.append((newDist, nextRow, nextCol))
                }
            }
        }
        return -1
    }
}
