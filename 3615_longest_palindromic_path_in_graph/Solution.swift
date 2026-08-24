// LeetCode 3615 - Longest Palindromic Path in Graph
// https://leetcode.com/problems/longest-palindromic-path-in-graph/

class Solution {
    func pack(_ a: Int, _ b: Int) -> Int { (a << 32) | b }

    func expandPal(_ g: [[Int]], _ label: [Character], _ l: Int, _ r: Int) -> Int {
        var vis = Set<Int>()
        var q = [[l, r, l != r ? 2 : 1]]
        var best = l != r ? 2 : 1
        vis.insert(pack(min(l, r), max(l, r)))
        var head = 0
        while head < q.count {
            let cur = q[head]; head += 1
            for a in g[cur[0]] {
                for b in g[cur[1]] {
                    if a == b || label[a] != label[b] { continue }
                    let p = pack(min(a, b), max(a, b))
                    if vis.contains(p) { continue }
                    vis.insert(p)
                    let nl = cur[2] + 2
                    best = max(best, nl)
                    q.append([a, b, nl])
                }
            }
        }
        return best
    }

    func maxLen(_ n: Int, _ edges: [[Int]], _ label: String) -> Int {
        var g = Array(repeating: [Int](), count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        let lab = Array(label)
        var ans = 1
        for i in 0..<n {
            ans = max(ans, expandPal(g, lab, i, i))
            for j in g[i] {
                if i < j && lab[i] == lab[j] {
                    ans = max(ans, expandPal(g, lab, i, j))
                }
            }
        }
        return ans
    }
}
