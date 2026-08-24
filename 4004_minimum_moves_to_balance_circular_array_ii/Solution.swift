// LeetCode 4004 - Minimum Moves to Balance Circular Array II
// https://leetcode.com/problems/minimum-moves-to-balance-circular-array-ii/


class Solution {
    func minMoves(_ balance: [Int]) -> Int {
        class Edge {
            var to: Int
            var cap: Int
            var cost: Int
            var rev: Int
            init(_ to: Int, _ cap: Int, _ cost: Int, _ rev: Int) {
                self.to = to; self.cap = cap; self.cost = cost; self.rev = rev
            }
        }
        class MinCostMaxFlow {
            let n: Int
            var graph: [[Edge]]
            let INF = 1_000_000_000
            init(_ n: Int) {
                self.n = n
                graph = Array(repeating: [Edge](), count: n)
            }
            func addEdge(_ u: Int, _ v: Int, _ cap: Int, _ cost: Int) {
                graph[u].append(Edge(v, cap, cost, graph[v].count))
                graph[v].append(Edge(u, 0, -cost, graph[u].count - 1))
            }
            func minCostFlow(_ source: Int, _ sink: Int, _ maxFlow: Int) -> Int {
                var totalCost = 0
                var currentFlow = 0
                while currentFlow < maxFlow {
                    var dist = Array(repeating: INF, count: n)
                    var parentNode = Array(repeating: -1, count: n)
                    var parentEdge = Array(repeating: -1, count: n)
                    var inQueue = Array(repeating: false, count: n)
                    var q = [source]
                    var head = 0
                    dist[source] = 0
                    inQueue[source] = true
                    while head < q.count {
                        let u = q[head]; head += 1
                        inQueue[u] = false
                        for i in 0..<graph[u].count {
                            let e = graph[u][i]
                            if e.cap > 0 && dist[e.to] > dist[u] + e.cost {
                                dist[e.to] = dist[u] + e.cost
                                parentNode[e.to] = u
                                parentEdge[e.to] = i
                                if !inQueue[e.to] {
                                    inQueue[e.to] = true
                                    q.append(e.to)
                                }
                            }
                        }
                    }
                    if dist[sink] == INF { return -1 }
                    var pushFlow = maxFlow - currentFlow
                    var cur = sink
                    while cur != source {
                        let e = graph[parentNode[cur]][parentEdge[cur]]
                        if e.cap < pushFlow { pushFlow = e.cap }
                        cur = parentNode[cur]
                    }
                    cur = sink
                    while cur != source {
                        let p = parentNode[cur]
                        let idx = parentEdge[cur]
                        let rev = graph[p][idx].rev
                        graph[p][idx].cap -= pushFlow
                        graph[cur][rev].cap += pushFlow
                        cur = parentNode[cur]
                    }
                    currentFlow += pushFlow
                    totalCost += pushFlow * dist[sink]
                }
                return totalCost
            }
        }
        var totalBalance = 0, totalDeficit = 0
        for x in balance {
            totalBalance += x
            if x < 0 { totalDeficit += -x }
        }
        if totalBalance < 0 { return -1 }
        if totalDeficit == 0 { return 0 }
        let n = balance.count
        let source = n, sink = n + 1
        let mcmf = MinCostMaxFlow(n + 2)
        let INF = 1_000_000_000
        for i in 0..<n {
            let x = balance[i]
            if x > 0 { mcmf.addEdge(source, i, x, 0) }
            else if x < 0 { mcmf.addEdge(i, sink, -x, 0) }
            mcmf.addEdge(i, (i + 1) % n, INF, 1)
            mcmf.addEdge(i, (i - 1 + n) % n, INF, 1)
        }
        return mcmf.minCostFlow(source, sink, totalDeficit)
    }
}
