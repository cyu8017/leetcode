// LeetCode 1928 - Minimum Cost to Reach Destination in Time
// https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/

class Solution {
    func minCost(_ maxTime: Int, _ edges: [[Int]], _ passingFee: [Int]) -> Int {
        let n = passingFee.count
        var graph = Array(repeating: [(Int, Int)](), count: n)
        for e in edges {
            graph[e[0]].append((e[1], e[2]))
            graph[e[1]].append((e[0], e[2]))
        }
        var minTime = Array(repeating: maxTime + 1, count: n)
        // min-heap by cost: (cost, time, node)
        var heap: [(Int, Int, Int)] = [(passingFee[0], 0, 0)]
        func push(_ item: (Int, Int, Int)) {
            heap.append(item)
            var i = heap.count - 1
            while i > 0 {
                let p = (i - 1) / 2
                if heap[p].0 <= heap[i].0 { break }
                heap.swapAt(p, i)
                i = p
            }
        }
        func pop() -> (Int, Int, Int) {
            let top = heap[0]
            let last = heap.removeLast()
            if !heap.isEmpty {
                heap[0] = last
                var i = 0
                while true {
                    var smallest = i
                    let l = 2 * i + 1, r = 2 * i + 2
                    if l < heap.count && heap[l].0 < heap[smallest].0 { smallest = l }
                    if r < heap.count && heap[r].0 < heap[smallest].0 { smallest = r }
                    if smallest == i { break }
                    heap.swapAt(i, smallest)
                    i = smallest
                }
            }
            return top
        }
        while !heap.isEmpty {
            let (cost, time, u) = pop()
            if time >= minTime[u] { continue }
            minTime[u] = time
            if u == n - 1 { return cost }
            for (v, dt) in graph[u] {
                let nt = time + dt
                if nt <= maxTime && nt < minTime[v] {
                    push((cost + passingFee[v], nt, v))
                }
            }
        }
        return -1
    }
}
