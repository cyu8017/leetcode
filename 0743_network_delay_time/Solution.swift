// LeetCode 0743 - Network Delay Time
// https://leetcode.com/problems/network-delay-time/

class Solution {
    func networkDelayTime(_ times: [[Int]], _ n: Int, _ k: Int) -> Int {
        var g = Array(repeating: [(Int, Int)](), count: n + 1)
        for t in times { g[t[0]].append((t[1], t[2])) }
        var dist = Array(repeating: Int.max / 4, count: n + 1)
        dist[k] = 0
        var heap = [[k, 0]]
        func push(_ v: [Int]) {
            heap.append(v)
            var i = heap.count - 1
            while i > 0 {
                let p = (i - 1) / 2
                if heap[p][1] <= heap[i][1] { break }
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
                    if l < heap.count && heap[l][1] < heap[best][1] { best = l }
                    if r < heap.count && heap[r][1] < heap[best][1] { best = r }
                    if best == i { break }
                    heap.swapAt(i, best); i = best
                }
            }
            return top
        }
        while !heap.isEmpty {
            let cur = pop()
            let u = cur[0], d = cur[1]
            if d > dist[u] { continue }
            for (v, w) in g[u] where d + w < dist[v] {
                dist[v] = d + w
                push([v, dist[v]])
            }
        }
        let best = dist[1...].max()!
        return best >= Int.max / 4 ? -1 : best
    }
}
