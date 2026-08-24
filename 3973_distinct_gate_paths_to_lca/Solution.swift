// LeetCode 3973 - Distinct Gate Paths to LCA
// https://leetcode.com/problems/distinct-gate-paths-to-lca/


class Solution {
    private let MOD = 1_000_000_007

    private func multiply(_ a: [[Int]], _ b: [[Int]]) -> [[Int]] {
        var c = [[0, 0], [0, 0]]
        for i in 0..<2 {
            for j in 0..<2 {
                for k in 0..<2 {
                    c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % MOD
                }
            }
        }
        return c
    }

    func gatePathXor(_ n: Int, _ parent: [Int], _ gates: [[Int]], _ queries: [[Int]]) -> Int {
        var logn = 1
        while (1 << logn) <= n { logn += 1 }
        var up = Array(repeating: Array(repeating: 0, count: n), count: logn)
        var product = Array(repeating: Array(repeating: [[0, 0], [0, 0]], count: n), count: logn)
        var children = Array(repeating: [Int](), count: n)
        for node in 1..<n { children[parent[node]].append(node) }
        var depth = Array(repeating: 0, count: n)
        var order = [0]
        var oi = 0
        while oi < order.count {
            let u = order[oi]
            for v in children[u] {
                depth[v] = depth[u] + 1
                order.append(v)
            }
            oi += 1
        }
        for u in 0..<n {
            up[0][u] = (u == 0) ? 0 : parent[u]
            product[0][u] = [
                [gates[u][1], gates[u][2]],
                [gates[u][2], gates[u][0]]
            ]
        }
        for level in 1..<logn {
            for u in 0..<n {
                let mid = up[level - 1][u]
                up[level][u] = up[level - 1][mid]
                product[level][u] = multiply(product[level - 1][u], product[level - 1][mid])
            }
        }
        func liftNode(_ node0: Int, _ distance0: Int) -> Int {
            var node = node0, distance = distance0, level = 0
            while distance > 0 {
                if (distance & 1) != 0 { node = up[level][node] }
                distance >>= 1
                level += 1
            }
            return node
        }
        func lca(_ a0: Int, _ b0: Int) -> Int {
            var a = a0, b = b0
            if depth[a] > depth[b] { a = liftNode(a, depth[a] - depth[b]) }
            else if depth[b] > depth[a] { b = liftNode(b, depth[b] - depth[a]) }
            if a == b { return a }
            for level in stride(from: logn - 1, through: 0, by: -1) {
                if up[level][a] != up[level][b] {
                    a = up[level][a]
                    b = up[level][b]
                }
            }
            return up[0][a]
        }
        func ways(_ node0: Int, _ card: Int, _ distance0: Int) -> Int {
            var node = node0, distance = distance0
            var vector = [0, 0]
            vector[card] = 1
            var level = 0
            while distance > 0 {
                if (distance & 1) != 0 {
                    let matrix = product[level][node]
                    vector = [
                        (vector[0] * matrix[0][0] + vector[1] * matrix[1][0]) % MOD,
                        (vector[0] * matrix[0][1] + vector[1] * matrix[1][1]) % MOD
                    ]
                    node = up[level][node]
                }
                distance >>= 1
                level += 1
            }
            return (vector[0] + vector[1]) % MOD
        }
        var answer = 0
        for query in queries {
            let ancestor = lca(query[0], query[2])
            let alice = ways(query[0], query[1], depth[query[0]] - depth[ancestor])
            let bob = ways(query[2], query[3], depth[query[2]] - depth[ancestor])
            let total = alice * bob % MOD
            answer ^= total
        }
        return answer
    }
}
