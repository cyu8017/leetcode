// LeetCode 0499 - The Maze III
// https://leetcode.com/problems/the-maze-iii/

import Foundation

private struct MazeState: Comparable {
    let dist: Int
    let path: String
    let row: Int
    let col: Int

    static func < (lhs: MazeState, rhs: MazeState) -> Bool {
        if lhs.dist != rhs.dist {
            return lhs.dist < rhs.dist
        }
        return lhs.path < rhs.path
    }
}

private struct MinHeap {
    private var data: [MazeState] = []

    var isEmpty: Bool { data.isEmpty }

    mutating func push(_ item: MazeState) {
        data.append(item)
        siftUp(data.count - 1)
    }

    mutating func pop() -> MazeState {
        let top = data[0]
        let last = data.removeLast()
        if !data.isEmpty {
            data[0] = last
            siftDown(0)
        }
        return top
    }

    private mutating func siftUp(_ index: Int) {
        var idx = index
        while idx > 0 {
            let parent = (idx - 1) / 2
            if data[parent] <= data[idx] {
                break
            }
            data.swapAt(parent, idx)
            idx = parent
        }
    }

    private mutating func siftDown(_ index: Int) {
        var idx = index
        while true {
            let left = idx * 2 + 1
            let right = left + 1
            var smallest = idx
            if left < data.count && data[left] < data[smallest] {
                smallest = left
            }
            if right < data.count && data[right] < data[smallest] {
                smallest = right
            }
            if smallest == idx {
                break
            }
            data.swapAt(idx, smallest)
            idx = smallest
        }
    }
}

class Solution {
    func findShortestWay(_ maze: [[Int]], _ ball: [Int], _ hole: [Int]) -> String {
        let rows = maze.count
        let cols = maze[0].count
        let holeRow = hole[0]
        let holeCol = hole[1]
        let directions: [(String, Int, Int)] = [
            ("d", 1, 0),
            ("l", 0, -1),
            ("r", 0, 1),
            ("u", -1, 0),
        ]

        func roll(_ row: Int, _ col: Int, _ dr: Int, _ dc: Int) -> (Int, Int, Int) {
            var nextRow = row
            var nextCol = col
            var distance = 0
            while nextRow + dr >= 0 && nextRow + dr < rows && nextCol + dc >= 0 && nextCol + dc < cols && maze[nextRow + dr][nextCol + dc] == 0 {
                nextRow += dr
                nextCol += dc
                distance += 1
                if nextRow == holeRow && nextCol == holeCol {
                    break
                }
            }
            return (nextRow, nextCol, distance)
        }

        var best: [String: (Int, String)] = [:]
        var heap = MinHeap()
        heap.push(MazeState(dist: 0, path: "", row: ball[0], col: ball[1]))

        while !heap.isEmpty {
            let current = heap.pop()
            let state = "\(current.row),\(current.col)"
            if let existing = best[state] {
                if existing.0 < current.dist || (existing.0 == current.dist && existing.1 <= current.path) {
                    continue
                }
            }
            best[state] = (current.dist, current.path)
            if current.row == holeRow && current.col == holeCol {
                return current.path
            }

            for (direction, dr, dc) in directions {
                let rolled = roll(current.row, current.col, dr, dc)
                if rolled.0 == current.row && rolled.1 == current.col {
                    continue
                }
                let newDist = current.dist + rolled.2
                let newPath = current.path + direction
                let target = "\(rolled.0),\(rolled.1)"
                if let existing = best[target] {
                    if newDist > existing.0 || (newDist == existing.0 && newPath >= existing.1) {
                        continue
                    }
                }
                heap.push(MazeState(dist: newDist, path: newPath, row: rolled.0, col: rolled.1))
            }
        }

        return "impossible"
    }
}
