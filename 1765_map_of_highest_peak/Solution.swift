// LeetCode 1765 - Map of Highest Peak
// https://leetcode.com/problems/map-of-highest-peak/

class Solution {
    func highestPeak(_ isWater: [[Int]]) -> [[Int]] {
        let m = isWater.count
        let n = isWater[0].count
        var dist = Array(repeating: Array(repeating: -1, count: n), count: m)
        var queue = [(Int, Int)]()
        for i in 0..<m {
            for j in 0..<n {
                if isWater[i][j] == 1 {
                    dist[i][j] = 0
                    queue.append((i, j))
                }
            }
        }
        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        var head = 0
        while head < queue.count {
            let (i, j) = queue[head]
            head += 1
            for (di, dj) in dirs {
                let x = i + di
                let y = j + dj
                if x >= 0 && x < m && y >= 0 && y < n && dist[x][y] == -1 {
                    dist[x][y] = dist[i][j] + 1
                    queue.append((x, y))
                }
            }
        }
        return dist
    }
}
