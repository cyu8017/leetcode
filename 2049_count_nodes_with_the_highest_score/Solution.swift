// LeetCode 2049 - Count Nodes With the Highest Score
// https://leetcode.com/problems/count-nodes-with-the-highest-score/

class Solution {
    func countHighestScoreNodes(_ parents: [Int]) -> Int {
        let n = parents.count
        var children = [[Int]](repeating: [], count: n)
        for i in 1..<n { children[parents[i]].append(i) }
        var size = [Int](repeating: 0, count: n)
        func dfs(_ u: Int) -> Int {
            size[u] = 1
            for v in children[u] { size[u] += dfs(v) }
            return size[u]
        }
        _ = dfs(0)
        var best = 0, ans = 0
        for u in 0..<n {
            var score = 1
            for v in children[u] { score *= size[v] }
            let up = n - size[u]
            if up > 0 { score *= up }
            if score > best { best = score; ans = 1 }
            else if score == best { ans += 1 }
        }
        return ans
    }
}
