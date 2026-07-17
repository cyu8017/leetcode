// LeetCode 1766 - Tree of Coprimes
// https://leetcode.com/problems/tree-of-coprimes/

class Solution {
    func getCoprimes(_ nums: [Int], _ edges: [[Int]]) -> [Int] {
        let n = nums.count
        var adj = Array(repeating: [Int](), count: n)
        for e in edges {
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        }

        func gcd(_ a: Int, _ b: Int) -> Int {
            var (x, y) = (a, b)
            while y != 0 {
                (x, y) = (y, x % y)
            }
            return x
        }

        var ans = Array(repeating: -1, count: n)
        var path = Array(repeating: [(depth: Int, node: Int)](), count: 51)

        func dfs(_ node: Int, _ parent: Int, _ depth: Int) {
            var bestDepth = -1
            var bestNode = -1
            let val = nums[node]
            for d in 1...50 {
                if gcd(val, d) == 1, let cand = path[d].last {
                    if cand.depth > bestDepth {
                        bestDepth = cand.depth
                        bestNode = cand.node
                    }
                }
            }
            ans[node] = bestNode
            path[val].append((depth, node))
            for nxt in adj[node] where nxt != parent {
                dfs(nxt, node, depth + 1)
            }
            path[val].removeLast()
        }

        dfs(0, -1, 0)
        return ans
    }
}
