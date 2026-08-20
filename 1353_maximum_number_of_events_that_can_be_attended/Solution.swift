// LeetCode 1353 - Maximum Number of Events That Can Be Attended
// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

class Solution {
    func maxEvents(_ events: [[Int]]) -> Int {
        let events = events.sorted { $0[0] < $1[0] }
        var heap = [Int]() // min-heap of end days
        func push(_ x: Int) {
            heap.append(x)
            var i = heap.count - 1
            while i > 0 {
                let p = (i - 1) / 2
                if heap[p] <= heap[i] { break }
                heap.swapAt(p, i); i = p
            }
        }
        func pop() -> Int {
            let r = heap[0]
            let last = heap.removeLast()
            if !heap.isEmpty {
                heap[0] = last
                var i = 0
                while true {
                    var s = i
                    let l = 2 * i + 1, rgt = 2 * i + 2
                    if l < heap.count && heap[l] < heap[s] { s = l }
                    if rgt < heap.count && heap[rgt] < heap[s] { s = rgt }
                    if s == i { break }
                    heap.swapAt(i, s); i = s
                }
            }
            return r
        }
        var i = 0, ans = 0, day = 0
        while i < events.count || !heap.isEmpty {
            if heap.isEmpty { day = max(day, events[i][0]) }
            while i < events.count && events[i][0] <= day {
                push(events[i][1]); i += 1
            }
            while !heap.isEmpty && heap[0] < day { _ = pop() }
            if !heap.isEmpty {
                _ = pop()
                ans += 1
                day += 1
            }
        }
        return ans
    }
}
