// LeetCode 3715 - Sum of Perfect Square Ancestors
// https://leetcode.com/problems/sum-of-perfect-square-ancestors/

class Solution {
    var graph = [[Int]]()
    var ks = [Int]()
    var freq = [Int: Int]()
    var ans = 0

    func kernel(_ x0: Int) -> Int {
        var x = x0, res = 1
        var p = 2
        while p * p <= x {
            var cnt = 0
            while x % p == 0 { x /= p; cnt += 1 }
            if cnt % 2 == 1 { res *= p }
            p += 1
        }
        if x > 1 { res *= x }
        return res
    }

    func dfs(_ u: Int, _ p: Int) {
        ans += freq[ks[u]] ?? 0
        freq[ks[u], default: 0] += 1
        for v in graph[u] where v != p { dfs(v, u) }
        freq[ks[u], default: 0] -= 1
    }

    func sumOfAncestors(_ n: Int, _ edges: [[Int]], _ nums: [Int]) -> Int {
        graph = Array(repeating: [], count: n)
        for e in edges {
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        }
        ks = nums.map { kernel($0) }
        freq = [:]
        ans = 0
        dfs(0, -1)
        return ans
    }
}
