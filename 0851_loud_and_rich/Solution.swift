// LeetCode 0851 - Loud and Rich
// https://leetcode.com/problems/loud-and-rich/

class Solution {
    func loudAndRich(_ richer: [[Int]], _ quiet: [Int]) -> [Int] {
        let n = quiet.count
        var graph = Array(repeating: [Int](), count: n)
        for e in richer { graph[e[1]].append(e[0]) }
        var ans = Array(repeating: -1, count: n)
        func dfs(_ person: Int) -> Int {
            if ans[person] != -1 { return ans[person] }
            var best = person
            for richerPerson in graph[person] {
                let cand = dfs(richerPerson)
                if quiet[cand] < quiet[best] { best = cand }
            }
            ans[person] = best
            return best
        }
        for i in 0..<n { _ = dfs(i) }
        return ans
    }
}
