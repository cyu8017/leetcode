// LeetCode 1383 - Maximum Performance of a Team
// https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution {
    func maxPerformance(_ n: Int, _ speed: [Int], _ efficiency: [Int], _ k: Int) -> Int {
        let pairs = zip(efficiency, speed).sorted { $0.0 > $1.0 }
        var heap = [Int]() // min-heap
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
                    let l = 2 * i + 1, rg = 2 * i + 2
                    if l < heap.count && heap[l] < heap[s] { s = l }
                    if rg < heap.count && heap[rg] < heap[s] { s = rg }
                    if s == i { break }
                    heap.swapAt(i, s); i = s
                }
            }
            return r
        }
        var total = 0, ans = 0
        for (e, s) in pairs {
            push(s); total += s
            if heap.count > k { total -= pop() }
            ans = max(ans, total * e)
        }
        return ans % 1_000_000_007
    }
}
