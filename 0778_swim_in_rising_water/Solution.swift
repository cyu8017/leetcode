// LeetCode 0778 - Swim in Rising Water
// https://leetcode.com/problems/swim-in-rising-water/

class Solution {
    func swimInWater(_ grid: [[Int]]) -> Int {
        let n = grid.count
        var heap = [[grid[0][0], 0, 0]]
        var seen = Array(repeating: Array(repeating: false, count: n), count: n)
        seen[0][0] = true
        func push(_ v: [Int]) {
            heap.append(v)
            var i = heap.count - 1
            while i > 0 {
                let p = (i - 1) / 2
                if heap[p][0] <= heap[i][0] { break }
                heap.swapAt(p, i); i = p
            }
        }
        func pop() -> [Int] {
            let top = heap[0]
            let last = heap.removeLast()
            if !heap.isEmpty {
                heap[0] = last
                var i = 0
                while true {
                    var best = i
                    let l = 2 * i + 1, r = 2 * i + 2
                    if l < heap.count && heap[l][0] < heap[best][0] { best = l }
                    if r < heap.count && heap[r][0] < heap[best][0] { best = r }
                    if best == i { break }
                    heap.swapAt(i, best); i = best
                }
            }
            return top
        }
        let dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while !heap.isEmpty {
            let cur = pop()
            let time = cur[0], r = cur[1], c = cur[2]
            if r == n - 1 && c == n - 1 { return time }
            for (dr, dc) in dirs {
                let nr = r + dr, nc = c + dc
                if nr >= 0 && nr < n && nc >= 0 && nc < n && !seen[nr][nc] {
                    seen[nr][nc] = true
                    push([max(time, grid[nr][nc]), nr, nc])
                }
            }
        }
        return -1
    }
}
