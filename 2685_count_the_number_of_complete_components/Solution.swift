// LeetCode 2685 - Count the Number of Complete Components
// https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution {
    func countCompleteComponents(_ n: Int, _ edges: [[Int]]) -> Int {
        var g = Array(repeating: [Int](), count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        var seen = Array(repeating: false, count: n)
        var ans = 0
        for i in 0..<n where !seen[i] {
            var nodes: [Int] = []
            var q = [i]
            seen[i] = true
            while !q.isEmpty {
                let u = q.removeFirst()
                nodes.append(u)
                for v in g[u] where !seen[v] {
                    seen[v] = true
                    q.append(v)
                }
            }
            let sz = nodes.count
            var ok = true
            for u in nodes where g[u].count != sz - 1 {
                ok = false
                break
            }
            if ok { ans += 1 }
        }
        return ans
    }
}
