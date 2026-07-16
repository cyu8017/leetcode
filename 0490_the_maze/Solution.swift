// LeetCode 0490 - The Maze
// https://leetcode.com/problems/the-maze/

class Solution {
    func hasPath(_ maze: [[Int]], _ start: [Int], _ destination: [Int]) -> Bool {
        let rows = maze.count
        let cols = maze[0].count
        let directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        var visited: Set<String> = []
        var stack = [(start[0], start[1])]

        while !stack.isEmpty {
            let (row, col) = stack.removeLast()
            let key = "\(row),\(col)"
            if visited.contains(key) {
                continue
            }
            visited.insert(key)
            if row == destination[0] && col == destination[1] {
                return true
            }
            for (dr, dc) in directions {
                var nr = row
                var nc = col
                while nr + dr >= 0 && nr + dr < rows && nc + dc >= 0 && nc + dc < cols && maze[nr + dr][nc + dc] == 0 {
                    nr += dr
                    nc += dc
                }
                let nextKey = "\(nr),\(nc)"
                if !visited.contains(nextKey) {
                    stack.append((nr, nc))
                }
            }
        }
        return false
    }
}
