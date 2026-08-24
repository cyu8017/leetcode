// LeetCode 2473 - Minimum Cost to Buy Apples
// https://leetcode.com/problems/minimum-cost-to-buy-apples/

class Solution {
    func minCost(_ n: Int, _ roads: [[Int]], _ appleCost: [Int], _ k: Int) -> [Int] {
        var g = [[(Int, Int)]](repeating: [], count: n + 1)
        for r in roads {
            g[r[0]].append((r[1], r[2]))
            g[r[1]].append((r[0], r[2]))
        }
        var heap = MinHeap<(Int, Int)> { $0.0 != $1.0 ? $0.0 < $1.0 : $0.1 < $1.1 }
        var ans = [Int](repeating: 0, count: n)
        let INF = Int.max / 4
        for start in 1...n {
            var dist = [Int](repeating: INF, count: n + 1)
            dist[start] = 0
            heap = MinHeap<(Int, Int)> { $0.0 != $1.0 ? $0.0 < $1.0 : $0.1 < $1.1 }
            heap.push((0, start))
            while !heap.isEmpty {
                let (d, u) = heap.pop()
                if d != dist[u] { continue }
                for (v, w) in g[u] {
                    let nd = d + w
                    if nd < dist[v] {
                        dist[v] = nd
                        heap.push((nd, v))
                    }
                }
            }
            var best = INF
            for city in 1...n {
                best = min(best, dist[city] * (k + 1) + appleCost[city - 1])
            }
            ans[start - 1] = best
        }
        return ans
    }

    private struct MinHeap<T> {
        var data = [T]()
        let less: (T, T) -> Bool
        init(_ less: @escaping (T, T) -> Bool) { self.less = less }
        var isEmpty: Bool { data.isEmpty }
        mutating func push(_ x: T) {
            data.append(x)
            var i = data.count - 1
            while i > 0 {
                let p = (i - 1) / 2
                if !less(data[i], data[p]) { break }
                data.swapAt(i, p)
                i = p
            }
        }
        mutating func pop() -> T {
            let res = data[0]
            let last = data.removeLast()
            if !data.isEmpty {
                data[0] = last
                var i = 0
                while true {
                    var smallest = i
                    let l = 2 * i + 1, r = 2 * i + 2
                    if l < data.count && less(data[l], data[smallest]) { smallest = l }
                    if r < data.count && less(data[r], data[smallest]) { smallest = r }
                    if smallest == i { break }
                    data.swapAt(i, smallest)
                    i = smallest
                }
            }
            return res
        }
    }
}
