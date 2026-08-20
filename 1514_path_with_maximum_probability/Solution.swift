// LeetCode 1514 - Path with Maximum Probability
// https://leetcode.com/problems/path-with-maximum-probability/

class Solution {
    func maxProbability(_ n: Int, _ edges: [[Int]], _ succProb: [Double], _ start_node: Int, _ end_node: Int) -> Double {
        var graph = Array(repeating: [(Int, Double)](), count: n)
        for (i, e) in edges.enumerated() {
            graph[e[0]].append((e[1], succProb[i]))
            graph[e[1]].append((e[0], succProb[i]))
        }
        var best = Array(repeating: 0.0, count: n)
        best[start_node] = 1.0
        var heap = [(prob: Double, node: Int)]()
        heap.append((1.0, start_node))
        while !heap.isEmpty {
            heap.sort { $0.prob > $1.prob }
            let cur = heap.removeFirst()
            if cur.node == end_node { return cur.prob }
            if cur.prob < best[cur.node] { continue }
            for (nei, ep) in graph[cur.node] {
                let candidate = cur.prob * ep
                if candidate > best[nei] {
                    best[nei] = candidate
                    heap.append((candidate, nei))
                }
            }
        }
        return 0.0
    }
}
