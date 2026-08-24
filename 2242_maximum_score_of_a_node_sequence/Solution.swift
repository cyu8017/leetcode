// LeetCode 2242 - Maximum Score of a Node Sequence
// https://leetcode.com/problems/maximum-score-of-a-node-sequence/

class Solution {
    func maximumScore(_ scores: [Int], _ edges: [[Int]]) -> Int {
        let n = scores.count
        var top = [[Int]](repeating: [], count: n)
        var g = [[Int]](repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        for i in 0..<n {
            for v in g[i] {
                top[i].append(v)
                var j = top[i].count - 1
                while j > 0 && scores[top[i][j]] > scores[top[i][j - 1]] {
                    top[i].swapAt(j, j - 1)
                    j -= 1
                }
                if top[i].count > 3 { top[i] = Array(top[i].prefix(3)) }
            }
        }
        var ans = -1
        for e in edges {
            let a = e[0], b = e[1]
            for c in top[a] where c != b {
                for d in top[b] where d != a && d != c {
                    ans = max(ans, scores[a] + scores[b] + scores[c] + scores[d])
                }
            }
        }
        return ans
    }
}
