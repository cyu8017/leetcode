// LeetCode 3841 - Palindromic Path Queries in a Tree
// https://leetcode.com/problems/palindromic-path-queries-in-a-tree/

class Solution {
    private var bit = [Int]()
    private var n = 0
    private var parent = [Int]()
    private var depth = [Int]()
    private var size = [Int]()
    private var heavy = [Int]()
    private var head = [Int]()
    private var position = [Int]()
    private var graph = [[Int]]()

    func palindromicPathQueries(_ n: Int, _ edges: [[Int]], _ s: String, _ queries: [String]) -> [Bool] {
        self.n = n
        graph = [[Int]](repeating: [], count: n)
        for edge in edges {
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        }
        parent = [Int](repeating: -2, count: n)
        depth = [Int](repeating: 0, count: n)
        parent[0] = -1
        var order = [0]
        var i = 0
        while i < order.count {
            let u = order[i]
            for v in graph[u] {
                if parent[v] == -2 {
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    order.append(v)
                }
            }
            i += 1
        }
        size = [Int](repeating: 0, count: n)
        heavy = [Int](repeating: -1, count: n)
        for i in stride(from: n - 1, through: 0, by: -1) {
            let u = order[i]
            size[u] = 1
            for v in graph[u] {
                if parent[v] == u {
                    size[u] += size[v]
                    if heavy[u] == -1 || size[v] > size[heavy[u]] { heavy[u] = v }
                }
            }
        }
        head = [Int](repeating: 0, count: n)
        position = [Int](repeating: 0, count: n)
        var stack = [[0, 0]]
        var nextPosition = 0
        while !stack.isEmpty {
            let chain = stack.removeLast()
            var u = chain[0]
            while u != -1 {
                head[u] = chain[1]
                position[u] = nextPosition
                nextPosition += 1
                for v in graph[u] {
                    if parent[v] == u && v != heavy[u] { stack.append([v, v]) }
                }
                u = heavy[u]
            }
        }
        bit = [Int](repeating: 0, count: n + 1)
        var current = Array(s)
        for node in 0..<n {
            update(position[node], 1 << Int(current[node].asciiValue! - 97))
        }
        var answer = [Bool]()
        for query in queries {
            let parts = query.split(separator: " ").map(String.init)
            let op = parts[0]
            let node = Int(parts[1])!
            if op == "update" {
                let newCharacter = parts[2].first!
                let delta = (1 << Int(current[node].asciiValue! - 97)) ^ (1 << Int(newCharacter.asciiValue! - 97))
                update(position[node], delta)
                current[node] = newCharacter
            } else {
                let other = Int(parts[2])!
                let mask = pathMask(node, other)
                answer.append((mask & (mask - 1)) == 0)
            }
        }
        return answer
    }

    private func update(_ index: Int, _ value: Int) {
        var index = index + 1
        while index <= n {
            bit[index] ^= value
            index += index & -index
        }
    }

    private func prefix(_ index: Int) -> Int {
        var index = index, result = 0
        while index > 0 {
            result ^= bit[index]
            index -= index & -index
        }
        return result
    }

    private func pathMask(_ u: Int, _ v: Int) -> Int {
        var u = u, v = v, result = 0
        while head[u] != head[v] {
            if depth[head[u]] < depth[head[v]] { swap(&u, &v) }
            result ^= prefix(position[u] + 1) ^ prefix(position[head[u]])
            u = parent[head[u]]
        }
        if position[u] > position[v] { swap(&u, &v) }
        return result ^ prefix(position[v] + 1) ^ prefix(position[u])
    }
}
