// LeetCode 1786 - Number of Restricted Paths From First to Last Node
// https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/

class Solution {
    func countRestrictedPaths(_ n: Int, _ edges: [[Int]]) -> Int {
        var adj = Array(repeating: [(Int, Int)](), count: n + 1)
        for e in edges {
            adj[e[0]].append((e[1], e[2]))
            adj[e[1]].append((e[0], e[2]))
        }
        var dist = Array(repeating: Int.max, count: n + 1)
        dist[n] = 0
        var heap: [(Int, Int)] = [(0, n)]
        func push(_ item: (Int, Int)) {
            heap.append(item)
            var i = heap.count - 1
            while i > 0 {
                let parent = (i - 1) / 2
                if heap[parent].0 <= heap[i].0 {
                    break
                }
                heap.swapAt(parent, i)
                i = parent
            }
        }
        func pop() -> (Int, Int) {
            let top = heap[0]
            let last = heap.removeLast()
            if !heap.isEmpty {
                heap[0] = last
                var i = 0
                while true {
                    var smallest = i
                    let l = 2 * i + 1
                    let r = 2 * i + 2
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
            let (d, u) = pop()
            if d != dist[u] {
                continue
            }
            for (v, w) in adj[u] {
                let nd = d + w
                if nd < dist[v] {
                    dist[v] = nd
                    push((nd, v))
                }
            }
        }
        let order = (1...n).sorted { dist[$0] < dist[$1] }
        let mod = 1_000_000_007
        var cnt = Array(repeating: 0, count: n + 1)
        cnt[n] = 1
        for u in order where u != n {
            for (v, _) in adj[u] {
                if dist[u] > dist[v] {
                    cnt[u] = (cnt[u] + cnt[v]) % mod
                }
            }
        }
        return cnt[1]
    }
}
