// LeetCode 2479 - Maximum XOR of Two Non-Overlapping Subtrees
// https://leetcode.com/problems/maximum-xor-of-two-non-overlapping-subtrees/

class Solution {
    func maxXor(_ n: Int, _ edges: [[Int]], _ values: [Int]) -> Int {
        class Trie {
            var child = [Trie?](repeating: nil, count: 2)
        }
        var g = [[Int]](repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        var sum = [Int](repeating: 0, count: n)
        func dfsSum(_ u: Int, _ p: Int) -> Int {
            var s = values[u]
            for v in g[u] where v != p { s += dfsSum(v, u) }
            sum[u] = s
            return s
        }
        _ = dfsSum(0, -1)
        let root = Trie()
        func insert(_ x: Int) {
            var cur = root
            for b in stride(from: 46, through: 0, by: -1) {
                let bit = (x >> b) & 1
                if cur.child[bit] == nil { cur.child[bit] = Trie() }
                cur = cur.child[bit]!
            }
        }
        func query(_ x: Int) -> Int {
            var cur = root
            if cur.child[0] == nil && cur.child[1] == nil { return 0 }
            var res = 0
            for b in stride(from: 46, through: 0, by: -1) {
                let bit = (x >> b) & 1
                let want = bit ^ 1
                if cur.child[want] != nil {
                    res |= 1 << b
                    cur = cur.child[want]!
                } else if cur.child[bit] != nil {
                    cur = cur.child[bit]!
                } else {
                    return res
                }
            }
            return res
        }
        var ans = 0
        func dfs(_ u: Int, _ p: Int) {
            for v in g[u] where v != p {
                ans = max(ans, query(sum[v]))
                dfs(v, u)
                insert(sum[v])
            }
        }
        dfs(0, -1)
        return ans
    }
}
