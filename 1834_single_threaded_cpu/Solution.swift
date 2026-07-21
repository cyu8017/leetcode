// LeetCode 1834 - Single-Threaded CPU
// https://leetcode.com/problems/single-threaded-cpu/

class Solution {
    func getOrder(_ tasks: [[Int]]) -> [Int] {
        let n = tasks.count
        var indexed = (0..<n).map { ($0, tasks[$0][0], tasks[$0][1]) }
        indexed.sort { a, b in
            if a.1 != b.1 { return a.1 < b.1 }
            return a.0 < b.0
        }
        var heap: [(Int, Int)] = []
        func push(_ duration: Int, _ idx: Int) {
            heap.append((duration, idx))
            var i = heap.count - 1
            while i > 0 {
                let p = (i - 1) / 2
                let better = heap[i].0 < heap[p].0 || (heap[i].0 == heap[p].0 && heap[i].1 < heap[p].1)
                if !better { break }
                heap.swapAt(p, i)
                i = p
            }
        }
        func pop() -> (Int, Int) {
            let top = heap[0]
            let last = heap.removeLast()
            if !heap.isEmpty {
                heap[0] = last
                var i = 0
                while true {
                    var best = i
                    let l = 2 * i + 1, r = 2 * i + 2
                    if l < heap.count {
                        let better = heap[l].0 < heap[best].0 || (heap[l].0 == heap[best].0 && heap[l].1 < heap[best].1)
                        if better { best = l }
                    }
                    if r < heap.count {
                        let better = heap[r].0 < heap[best].0 || (heap[r].0 == heap[best].0 && heap[r].1 < heap[best].1)
                        if better { best = r }
                    }
                    if best == i { break }
                    heap.swapAt(i, best)
                    i = best
                }
            }
            return top
        }

        var i = 0
        var time = 0
        var order = [Int]()
        while i < n || !heap.isEmpty {
            if i < n && heap.isEmpty {
                time = max(time, indexed[i].1)
            }
            while i < n && indexed[i].1 <= time {
                push(indexed[i].2, indexed[i].0)
                i += 1
            }
            let (duration, idx) = pop()
            time += duration
            order.append(idx)
        }
        return order
    }
}
