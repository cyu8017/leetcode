// LeetCode 3123 - Find Edges in Shortest Paths
// https://leetcode.com/problems/find-edges-in-shortest-paths/

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
    func findAnswer(_ n: Int, _ edges: [[Int]]) -> [Bool] {
        var g = Array(repeating: [(Int, Int, Int)](), count: n)
        for i in 0..<edges.count {
            let a = edges[i][0], b = edges[i][1], w = edges[i][2]
            g[a].append((b, w, i))
            g[b].append((a, w, i))
        }
        let INF = 1 << 30
        var dist = Array(repeating: INF, count: n)
        dist[0] = 0
        var pq = MinHeap()
        pq.push((0, 0))
        while !pq.isEmpty {
            let (da, a) = pq.pop()
            if da > dist[a] { continue }
            for (b, w, _) in g[a] where dist[b] > dist[a] + w {
                dist[b] = dist[a] + w
                pq.push((dist[b], b))
            }
        }
        var ans = Array(repeating: false, count: edges.count)
        if dist[n - 1] == INF { return ans }
        var q = [n - 1]
        var qi = 0
        while qi < q.count {
            let a = q[qi]; qi += 1
            for (b, w, i) in g[a] where dist[a] == dist[b] + w {
                ans[i] = true
                q.append(b)
            }
        }
        return ans
    }
}
