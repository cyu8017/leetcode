// LeetCode 2203 - Minimum Weighted Subgraph With the Required Paths
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/

private struct HeapNode: Comparable {
    let d: Int
    let u: Int
    static func < (lhs: HeapNode, rhs: HeapNode) -> Bool { lhs.d < rhs.d }
}

private struct MinHeap {
    private var data: [HeapNode] = []
    var isEmpty: Bool { data.isEmpty }
    mutating func push(_ x: HeapNode) {
        data.append(x)
        siftUp(data.count - 1)
    }
    mutating func pop() -> HeapNode {
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
            if data[p] <= data[idx] { break }
            data.swapAt(p, idx)
            idx = p
        }
    }
    private mutating func siftDown(_ i: Int) {
        var idx = i
        while true {
            var smallest = idx
            let l = idx * 2 + 1, r = idx * 2 + 2
            if l < data.count && data[l] < data[smallest] { smallest = l }
            if r < data.count && data[r] < data[smallest] { smallest = r }
            if smallest == idx { break }
            data.swapAt(smallest, idx)
            idx = smallest
        }
    }
}

class Solution {
    func minimumWeight(_ n: Int, _ edges: [[Int]], _ src1: Int, _ src2: Int, _ dest: Int) -> Int {
        var g = [[(Int, Int)]](repeating: [], count: n)
        var rg = [[(Int, Int)]](repeating: [], count: n)
        for e in edges {
            g[e[0]].append((e[1], e[2]))
            rg[e[1]].append((e[0], e[2]))
        }
        let inf = Int.max / 4
        func dijkstra(_ graph: [[(Int, Int)]], _ src: Int) -> [Int] {
            var dist = [Int](repeating: inf, count: n)
            dist[src] = 0
            var pq = MinHeap()
            pq.push(HeapNode(d: 0, u: src))
            while !pq.isEmpty {
                let cur = pq.pop()
                if cur.d != dist[cur.u] { continue }
                for (v, w) in graph[cur.u] {
                    if cur.d + w < dist[v] {
                        dist[v] = cur.d + w
                        pq.push(HeapNode(d: dist[v], u: v))
                    }
                }
            }
            return dist
        }
        let d1 = dijkstra(g, src1)
        let d2 = dijkstra(g, src2)
        let dd = dijkstra(rg, dest)
        var ans = inf
        for i in 0..<n {
            if d1[i] >= inf || d2[i] >= inf || dd[i] >= inf { continue }
            ans = min(ans, d1[i] + d2[i] + dd[i])
        }
        return ans >= inf ? -1 : ans
    }
}
