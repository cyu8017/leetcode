// LeetCode 1606 - Find Servers That Handled Most Number of Requests
// https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/

private struct MinHeap<T: Comparable> {
    private var data = [T]()
    var isEmpty: Bool { data.isEmpty }
    var count: Int { data.count }
    mutating func push(_ value: T) {
        data.append(value)
        var i = data.count - 1
        while i > 0 {
            let p = (i - 1) / 2
            if data[p] <= data[i] { break }
            data.swapAt(p, i)
            i = p
        }
    }
    mutating func pop() -> T {
        let result = data[0]
        let last = data.removeLast()
        if !data.isEmpty {
            data[0] = last
            var i = 0
            while true {
                var best = i
                let l = 2 * i + 1, r = l + 1
                if l < data.count && data[l] < data[best] { best = l }
                if r < data.count && data[r] < data[best] { best = r }
                if best == i { break }
                data.swapAt(i, best)
                i = best
            }
        }
        return result
    }
    func peek() -> T? { data.first }
}

class Solution {
    func busiestServers(_ k: Int, _ arrival: [Int], _ load: [Int]) -> [Int] {
        var free = MinHeap<Int>()
        for i in 0..<k { free.push(i) }
        var busy = MinHeap<(Int, Int)>()
        var count = [Int](repeating: 0, count: k)
        for i in 0..<arrival.count {
            let t = arrival[i]
            while let top = busy.peek(), top.0 <= t {
                let server = busy.pop().1
                free.push(i + ((server - i) % k + k) % k)
            }
            if free.isEmpty { continue }
            let server = free.pop() % k
            count[server] += 1
            busy.push((t + load[i], server))
        }
        let best = count.max() ?? 0
        return count.indices.filter { count[$0] == best }
    }
}
