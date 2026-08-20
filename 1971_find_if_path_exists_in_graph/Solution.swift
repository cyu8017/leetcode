// LeetCode 1971 - Find if Path Exists in Graph
// https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution {
    func validPath(_ n: Int, _ edges: [[Int]], _ source: Int, _ destination: Int) -> Bool {
        if source == destination { return true }
        var g = Array(repeating: [Int](), count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        var stack = [source]
        var seen: Set<Int> = [source]
        while !stack.isEmpty {
            let u = stack.removeLast()
            if u == destination { return true }
            for v in g[u] where !seen.contains(v) {
                seen.insert(v)
                stack.append(v)
            }
        }
        return false
    }
}
