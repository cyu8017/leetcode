// LeetCode 0407 - Trapping Rain Water II
// https://leetcode.com/problems/trapping-rain-water-ii/

class Solution {
    func trapRainWater(_ heightMap: [[Int]]) -> Int {
        if heightMap.isEmpty || heightMap[0].isEmpty {
            return 0
        }

        let rows = heightMap.count
        let cols = heightMap[0].count
        if rows < 3 || cols < 3 {
            return 0
        }

        var visited = Array(repeating: Array(repeating: false, count: cols), count: rows)
        var heap: [(Int, Int, Int)] = []

        for row in 0..<rows {
            for col in 0..<cols where row == 0 || row == rows - 1 || col == 0 || col == cols - 1 {
                heapPush(&heap, (heightMap[row][col], row, col))
                visited[row][col] = true
            }
        }

        var trapped = 0
        let directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while !heap.isEmpty {
            let (height, row, col) = heapPop(&heap)
            for (dr, dc) in directions {
                let nextRow = row + dr
                let nextCol = col + dc
                if nextRow < 0 || nextRow >= rows || nextCol < 0 || nextCol >= cols {
                    continue
                }
                if visited[nextRow][nextCol] {
                    continue
                }

                visited[nextRow][nextCol] = true
                let nextHeight = heightMap[nextRow][nextCol]
                trapped += max(0, height - nextHeight)
                heapPush(&heap, (max(height, nextHeight), nextRow, nextCol))
            }
        }

        return trapped
    }

    private func heapPush(_ heap: inout [(Int, Int, Int)], _ item: (Int, Int, Int)) {
        heap.append(item)
        var index = heap.count - 1
        while index > 0 {
            let parent = (index - 1) / 2
            if heap[parent].0 <= heap[index].0 {
                break
            }
            heap.swapAt(parent, index)
            index = parent
        }
    }

    private func heapPop(_ heap: inout [(Int, Int, Int)]) -> (Int, Int, Int) {
        let top = heap[0]
        let last = heap.removeLast()
        if heap.isEmpty {
            return top
        }
        heap[0] = last
        var index = 0
        while true {
            var smallest = index
            let left = index * 2 + 1
            let right = index * 2 + 2
            if left < heap.count && heap[left].0 < heap[smallest].0 {
                smallest = left
            }
            if right < heap.count && heap[right].0 < heap[smallest].0 {
                smallest = right
            }
            if smallest == index {
                break
            }
            heap.swapAt(smallest, index)
            index = smallest
        }
        return top
    }
}
