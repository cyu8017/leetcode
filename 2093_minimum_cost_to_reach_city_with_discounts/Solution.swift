// LeetCode 2093 - Minimum Cost to Reach City With Discounts
// https://leetcode.com/problems/minimum-cost-to-reach-city-with-discounts/

class Solution {
    func minimumCost(_ n: Int, _ highways: [[Int]], _ discounts: Int) -> Int {
        var g = [[(Int, Int)]](repeating: [], count: n)
        for h in highways {
            g[h[0]].append((h[1], h[2]))
            g[h[1]].append((h[0], h[2]))
        }
        let INF = 1 << 30
        var dist = [[Int]](repeating: [Int](repeating: INF, count: discounts + 1), count: n)
        var heap = [(Int, Int, Int)]()
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
            heap[0] = heap.removeLast()
            if !heap.isEmpty {
                var i = 0
                while true {
                    var best = i
                    let l = 2 * i + 1, r = 2 * i + 2
                    if l < heap.count && heap[l].0 < heap[best].0 { best = l }
                    if r < heap.count && heap[r].0 < heap[best].0 { best = r }
                    if best == i { break }
                    heap.swapAt(i, best)
                    i = best
                }
            }
            return top
        }
        dist[0][discounts] = 0
        push((0, 0, discounts))
        while !heap.isEmpty {
            let (cost, city, disc) = pop()
            if city == n - 1 { return cost }
            if cost > dist[city][disc] { continue }
            for (v, w) in g[city] {
                if cost + w < dist[v][disc] {
                    dist[v][disc] = cost + w
                    push((dist[v][disc], v, disc))
                }
                if disc > 0 && cost + w / 2 < dist[v][disc - 1] {
                    dist[v][disc - 1] = cost + w / 2
                    push((dist[v][disc - 1], v, disc - 1))
                }
            }
        }
        return -1
    }
}
