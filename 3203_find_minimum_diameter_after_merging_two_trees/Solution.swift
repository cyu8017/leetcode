// LeetCode 3203 - Find Minimum Diameter After Merging Two Trees
// https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/

class Solution {
    private var ans = 0
    private var a = 0
    private var g: [[Int]] = []

    func minimumDiameterAfterMerge(_ edges1: [[Int]], _ edges2: [[Int]]) -> Int {
        let d1 = treeDiameter(edges1)
        let d2 = treeDiameter(edges2)
        return max(max(d1, d2), (d1 + 1) / 2 + (d2 + 1) / 2 + 1)
    }

    private func treeDiameter(_ edges: [[Int]]) -> Int {
        let n = edges.count + 1
        g = Array(repeating: [Int](), count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        ans = 0
        a = 0
        dfs(0, -1, 0)
        dfs(a, -1, 0)
        return ans
    }

    private func dfs(_ i: Int, _ fa: Int, _ t: Int) {
        for j in g[i] where j != fa { dfs(j, i, t + 1) }
        if ans < t {
            ans = t
            a = i
        }
    }
}
