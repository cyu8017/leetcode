// LeetCode 2503 - Maximum Number of Points From Grid Queries
// https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/

class Solution {
    func maxPoints(_ grid: [[Int]], _ queries: [Int]) -> [Int] {
        let m = grid.count, n = grid[0].count
        var order = Array(0..<queries.count)
        order.sort { queries[$0] < queries[$1] }
        var ans = [Int](repeating: 0, count: queries.count)
        var visited = [[Bool]](repeating: [Bool](repeating: false, count: n), count: m)
        var pq = MinHeap<(Int, Int, Int)> { $0.0 < $1.0 }
        pq.push((grid[0][0], 0, 0))
        visited[0][0] = true
        var points = 0
        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for qi in order {
            let q = queries[qi]
            while !pq.isEmpty && pq.peek()!.0 < q {
                let cell = pq.pop()
                let r = cell.1, c = cell.2
                points += 1
                for d in dirs {
                    let nr = r + d.0, nc = c + d.1
                    if nr >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr][nc] {
                        visited[nr][nc] = true
                        pq.push((grid[nr][nc], nr, nc))
                    }
                }
            }
            ans[qi] = points
        }
        return ans
    }

    private struct MinHeap<T> {
        var data = [T]()
        let less: (T, T) -> Bool
        init(_ less: @escaping (T, T) -> Bool) { self.less = less }
        var isEmpty: Bool { data.isEmpty }
        func peek() -> T? { data.first }
        mutating func push(_ x: T) {
            data.append(x)
            var i = data.count - 1
            while i > 0 {
                let p = (i - 1) / 2
                if !less(data[i], data[p]) { break }
                data.swapAt(i, p)
                i = p
            }
        }
        mutating func pop() -> T {
            let res = data[0]
            let last = data.removeLast()
            if !data.isEmpty {
                data[0] = last
                var i = 0
                while true {
                    var smallest = i
                    let l = 2 * i + 1, r = 2 * i + 2
                    if l < data.count && less(data[l], data[smallest]) { smallest = l }
                    if r < data.count && less(data[r], data[smallest]) { smallest = r }
                    if smallest == i { break }
                    data.swapAt(i, smallest)
                    i = smallest
                }
            }
            return res
        }
    }

}
