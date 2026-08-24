// LeetCode 2581 - Count Number of Possible Root Nodes
// https://leetcode.com/problems/count-number-of-possible-root-nodes/

class Solution {
    func rootCount(_ edges: [[Int]], _ guesses: [[Int]], _ k: Int) -> Int {
        let n = edges.count + 1
        var g = [[Int]](repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        var guessSet = Set<Int>()
        func pack(_ a: Int, _ b: Int) -> Int { a * 100003 + b }
        for gu in guesses { guessSet.insert(pack(gu[0], gu[1])) }
        func dfs1(_ u: Int, _ p: Int) -> Int {
            var cnt = 0
            for v in g[u] where v != p {
                if guessSet.contains(pack(u, v)) { cnt += 1 }
                cnt += dfs1(v, u)
            }
            return cnt
        }
        var ans = 0
        func dfs2(_ u: Int, _ p: Int, _ cur: Int) {
            if cur >= k { ans += 1 }
            for v in g[u] where v != p {
                var nxt = cur
                if guessSet.contains(pack(u, v)) { nxt -= 1 }
                if guessSet.contains(pack(v, u)) { nxt += 1 }
                dfs2(v, u, nxt)
            }
        }
        dfs2(0, -1, dfs1(0, -1))
        return ans
    }
}
