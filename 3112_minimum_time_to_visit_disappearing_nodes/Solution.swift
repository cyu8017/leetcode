// LeetCode 3112 - Minimum Time to Visit Disappearing Nodes
// https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/

private struct MinHeap {
    private var data: [(Int, Int)] = []
    var isEmpty: Bool { data.isEmpty }
    mutating func push(_ x: (Int, Int)) {
        data.append(x)
        siftUp(data.count - 1)
    }
    mutating func pop() -> (Int, Int) {
        let top = data[0]
        let last = data.removeLast()
        if !data.isEmpty {
            data[0] = last
            siftDown(0)
        }
        return top
    }
    private mutating func siftUp(_ i: Int) {
        var idx = i
        while idx > 0 {
            let p = (idx - 1) / 2
            if data[p].0 <= data[idx].0 { break }
            data.swapAt(p, idx)
            idx = p
        }
    }
    private mutating func siftDown(_ i: Int) {
        var idx = i
        while true {
            var smallest = idx
            let l = idx * 2 + 1, r = idx * 2 + 2
            if l < data.count && data[l].0 < data[smallest].0 { smallest = l }
            if r < data.count && data[r].0 < data[smallest].0 { smallest = r }
            if smallest == idx { break }
            data.swapAt(smallest, idx)
            idx = smallest
        }
    }
}

class Solution {
    func minimumTime(_ n: Int, _ edges: [[Int]], _ disappear: [Int]) -> [Int] {
        var g = Array(repeating: [(Int, Int)](), count: n)
        for e in edges {
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))
        }
        let INF = 1 << 30
        var dist = Array(repeating: INF, count: n)
        dist[0] = 0
        var pq = MinHeap()
        pq.push((0, 0))
        while !pq.isEmpty {
            let (du, u) = pq.pop()
            if du > dist[u] { continue }
            for (v, w) in g[u] {
                if dist[v] > dist[u] + w && dist[u] + w < disappear[v] {
                    dist[v] = dist[u] + w
                    pq.push((dist[v], v))
                }
            }
        }
        return (0..<n).map { dist[$0] < disappear[$0] ? dist[$0] : -1 }
    }
}
