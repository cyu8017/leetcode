// LeetCode 2867 - Count Valid Paths in a Tree
// https://leetcode.com/problems/count-valid-paths-in-a-tree/

class Solution {
    private var isPrime: [Bool] = []
    private var g: [[Int]] = []

    func countPaths(_ n: Int, _ edges: [[Int]]) -> Int {
        isPrime = Array(repeating: true, count: n + 1)
        isPrime[0] = false
        isPrime[1] = false
        var i = 2
        while i * i <= n {
            if isPrime[i] {
                var j = i * i
                while j <= n {
                    isPrime[j] = false
                    j += i
                }
            }
            i += 1
        }
        g = Array(repeating: [], count: n + 1)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        var ans = 0
        for u in 1...n {
            if !isPrime[u] { continue }
            var total = 0
            for v in g[u] {
                let c = dfs(v, u)
                ans += c
                ans += total * c
                total += c
            }
        }
        return ans
    }

    private func dfs(_ u: Int, _ p: Int) -> Int {
        if isPrime[u] { return 0 }
        var sz = 1
        for v in g[u] where v != p {
            sz += dfs(v, u)
        }
        return sz
    }
}
