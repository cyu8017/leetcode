// LeetCode 3910 - Count Connected Subgraphs With Even Node Sum
// https://leetcode.com/problems/count-connected-subgraphs-with-even-node-sum/

class Solution {
    private var g = [[Int]]()
    private var vis = 0, m = 0

    func evenSumSubgraphs(_ nums: [Int], _ edges: [[Int]]) -> Int {
        let n = nums.count
        g = [[Int]](repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        m = (1 << n) - 1
        var ans = 0
        if m >= 1 {
            for sub in 1...m {
                var s = 0
                for i in 0..<n {
                    if ((sub >> i) & 1) != 0 { s += nums[i] }
                }
                if s % 2 != 0 { continue }
                vis = m ^ sub
                var start = 0, tmp = sub
                while tmp > 1 { tmp >>= 1; start += 1 }
                dfs(start)
                if vis == m { ans += 1 }
            }
        }
        return ans
    }

    private func dfs(_ u: Int) {
        vis |= 1 << u
        for v in g[u] {
            if ((vis >> v) & 1) == 0 { dfs(v) }
        }
    }
}
