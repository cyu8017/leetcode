// LeetCode 0305 - Number of Islands II
// https://leetcode.com/problems/number-of-islands-ii/

class Solution {
    private var parent: [Int: Int] = [:]
    private var rank: [Int: Int] = [:]

    func numIslands2(_ m: Int, _ n: Int, _ positions: [[Int]]) -> [Int] {
        parent = [:]
        rank = [:]
        let directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        var result: [Int] = []
        var islands = 0

        for position in positions {
            let row = position[0]
            let col = position[1]
            let index = row * n + col
            if parent[index] != nil {
                result.append(islands)
                continue
            }

            parent[index] = index
            rank[index] = 0
            islands += 1

            for (dr, dc) in directions {
                let nr = row + dr
                let nc = col + dc
                if nr < 0 || nr >= m || nc < 0 || nc >= n {
                    continue
                }
                let neighbor = nr * n + nc
                if parent[neighbor] == nil {
                    continue
                }
                if union(index, neighbor) {
                    islands -= 1
                }
            }
            result.append(islands)
        }
        return result
    }

    private func find(_ index: Int) -> Int {
        if parent[index] != index {
            parent[index] = find(parent[index]!)
        }
        return parent[index]!
    }

    private func union(_ left: Int, _ right: Int) -> Bool {
        var rootLeft = find(left)
        var rootRight = find(right)
        if rootLeft == rootRight {
            return false
        }
        if rank[rootLeft, default: 0] < rank[rootRight, default: 0] {
            swap(&rootLeft, &rootRight)
        }
        parent[rootRight] = rootLeft
        if rank[rootLeft, default: 0] == rank[rootRight, default: 0] {
            rank[rootLeft, default: 0] += 1
        }
        return true
    }
}
