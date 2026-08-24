// LeetCode 3967 - Finish Time of Tasks II
// https://leetcode.com/problems/finish-time-of-tasks-ii/


class Solution {
    private struct Edge {
        var to: Int
        var reverse: Int
    }

    private func combine(_ minimum: Int, _ maximum: Int, _ count: Int, _ base: Int) -> Int {
        if count == 0 { return base }
        return 2 * maximum - minimum + base
    }

    func minFinishTime(_ n: Int, _ edges: [[Int]], _ baseTime: [Int]) -> Int {
        var graph = Array(repeating: [Edge](), count: n)
        for edge in edges {
            let u = edge[0], v = edge[1]
            let iu = graph[u].count, iv = graph[v].count
            graph[u].append(Edge(to: v, reverse: iv))
            graph[v].append(Edge(to: u, reverse: iu))
        }
        var parent = Array(repeating: -2, count: n)
        var parentEdge = Array(repeating: 0, count: n)
        parent[0] = -1
        var order = [0]
        var oi = 0
        while oi < order.count {
            let u = order[oi]
            for edge in graph[u] {
                if parent[edge.to] == -2 {
                    parent[edge.to] = u
                    parentEdge[edge.to] = edge.reverse
                    order.append(edge.to)
                }
            }
            oi += 1
        }
        var incoming = Array(repeating: [Int](), count: n)
        for i in 0..<n { incoming[i] = Array(repeating: 0, count: graph[i].count) }
        for oii in stride(from: n - 1, through: 1, by: -1) {
            let u = order[oii]
            var minimum = Int.max / 4, maximum = -1, count = 0
            for edgeIndex in 0..<incoming[u].count {
                if edgeIndex == parentEdge[u] { continue }
                let value = incoming[u][edgeIndex]
                minimum = min(minimum, value)
                maximum = max(maximum, value)
                count += 1
            }
            let value = combine(minimum, maximum, count, baseTime[u])
            let parentNode = parent[u]
            let reverseIndex = graph[u][parentEdge[u]].reverse
            incoming[parentNode][reverseIndex] = value
        }
        var answer = Int.max / 4
        for u in order {
            var min1 = Int.max / 4, min2 = Int.max / 4, minIndex = -1
            var max1 = -1, max2 = -1, maxIndex = -1
            for i in 0..<incoming[u].count {
                let value = incoming[u][i]
                if value < min1 {
                    min2 = min1
                    min1 = value
                    minIndex = i
                } else if value < min2 {
                    min2 = value
                }
                if value > max1 {
                    max2 = max1
                    max1 = value
                    maxIndex = i
                } else if value > max2 {
                    max2 = value
                }
            }
            let rootValue = combine(min1, max1, graph[u].count, baseTime[u])
            answer = min(answer, rootValue)
            for i in 0..<graph[u].count {
                let edge = graph[u][i]
                if edge.to == parent[u] { continue }
                if graph[u].count == 1 {
                    incoming[edge.to][edge.reverse] = baseTime[u]
                    continue
                }
                var minimum = min1, maximum = max1
                if i == minIndex { minimum = min2 }
                if i == maxIndex { maximum = max2 }
                incoming[edge.to][edge.reverse] = combine(minimum, maximum, graph[u].count - 1, baseTime[u])
            }
        }
        return answer
    }
}
