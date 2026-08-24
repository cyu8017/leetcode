// LeetCode 3310 - Remove Methods From Project
// https://leetcode.com/problems/remove-methods-from-project/

class Solution {
    func remainingMethods(_ n: Int, _ k: Int, _ invocations: [[Int]]) -> [Int] {
        var g = Array(repeating: [Int](), count: n)
        for e in invocations { g[e[0]].append(e[1]) }
        var sus = Array(repeating: false, count: n)
        func dfs(_ u: Int) {
            if sus[u] { return }
            sus[u] = true
            for v in g[u] { dfs(v) }
        }
        dfs(k)
        for e in invocations {
            if !sus[e[0]] && sus[e[1]] {
                return Array(0..<n)
            }
        }
        return (0..<n).filter { !sus[$0] }
    }
}
