// LeetCode 2872 - Maximum Number of K-Divisible Components
// https://leetcode.com/problems/maximum-number-of-k-divisible-components/

class Solution {
    private var g: [[Int]] = []
    private var values: [Int] = []
    private var k = 0
    private var ans = 0

    func maxKDivisibleComponents(_ n: Int, _ edges: [[Int]], _ values: [Int], _ k: Int) -> Int {
        self.values = values
        self.k = k
        g = Array(repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        ans = 0
        dfs(0, -1)
        return ans
    }

    private func dfs(_ u: Int, _ p: Int) -> Int {
        var sum = values[u] % k
        for v in g[u] where v != p {
            sum = (sum + dfs(v, u)) % k
        }
        if sum == 0 { ans += 1 }
        return sum
    }
}
