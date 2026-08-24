// LeetCode 3004 - Maximum Subtree of the Same Color
// https://leetcode.com/problems/maximum-subtree-of-the-same-color/

class Solution {
    private var g: [[Int]] = []
    private var colors: [Int] = []
    private var size: [Int] = []
    private var ans = 0

    func maximumSubtreeSize(_ edges: [[Int]], _ colors: [Int]) -> Int {
        let n = edges.count + 1
        self.colors = colors
        g = Array(repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        size = Array(repeating: 0, count: n)
        ans = 0
        _ = dfs(0, -1)
        return ans
    }

    private func dfs(_ a: Int, _ fa: Int) -> Bool {
        size[a] = 1
        var ok = true
        for b in g[a] where b != fa {
            let t = dfs(b, a)
            ok = ok && t && colors[a] == colors[b]
            size[a] += size[b]
        }
        if ok { ans = max(ans, size[a]) }
        return ok
    }
}
