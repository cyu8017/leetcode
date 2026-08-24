// LeetCode 3812 - Minimum Edge Toggles On A Tree
// https://leetcode.com/problems/minimum-edge-toggles-on-a-tree/

class Solution {
    private var g = [[[Int]]]()
    private var start = [Character]()
    private var target = [Character]()
    private var ans = [Int]()

    func minimumFlips(_ n: Int, _ edges: [[Int]], _ start: String, _ target: String) -> [Int] {
        self.start = Array(start)
        self.target = Array(target)
        g = [[[Int]]](repeating: [], count: n)
        if n > 1 {
            for i in 0..<(n - 1) {
                let a = edges[i][0], b = edges[i][1]
                g[a].append([b, i])
                g[b].append([a, i])
            }
        }
        ans = []
        if dfs(0, -1) { return [-1] }
        return ans.sorted()
    }

    private func dfs(_ a: Int, _ fa: Int) -> Bool {
        var rev = start[a] != target[a]
        for e in g[a] {
            let b = e[0], i = e[1]
            if b != fa && dfs(b, a) {
                ans.append(i)
                rev = !rev
            }
        }
        return rev
    }
}
