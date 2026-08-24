// LeetCode 3249 - Count the Number of Good Nodes
// https://leetcode.com/problems/count-the-number-of-good-nodes/

class Solution {
    private var g: [[Int]] = []
    private var ans = 0

    func countGoodNodes(_ edges: [[Int]]) -> Int {
        let n = edges.count + 1
        g = Array(repeating: [Int](), count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        ans = 0
        _ = dfs(0, -1)
        return ans
    }

    private func dfs(_ a: Int, _ fa: Int) -> Int {
        var pre = -1, cnt = 1, ok = 1
        for b in g[a] where b != fa {
            let cur = dfs(b, a)
            cnt += cur
            if pre < 0 { pre = cur }
            else if pre != cur { ok = 0 }
        }
        ans += ok
        return cnt
    }
}
