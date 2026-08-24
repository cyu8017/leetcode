// LeetCode 2746 - Decremental String Concatenation
// https://leetcode.com/problems/decremental-string-concatenation/

class Solution {
    func minimizeConcatenatedLength(_ words: [String]) -> Int {
        let w0 = Array(words[0])
        var memo: [String: Int] = [:]
        return w0.count + dfs(words, 1, w0[0], w0[w0.count - 1], &memo)
    }

    private func dfs(_ words: [String], _ i: Int, _ first: Character, _ last: Character, _ memo: inout [String: Int]) -> Int {
        if i == words.count { return 0 }
        let key = "\(i),\(first),\(last)"
        if let v = memo[key] { return v }
        let w = Array(words[i])
        let wf = w[0], wl = w[w.count - 1]
        let add1 = w.count - (last == wf ? 1 : 0)
        let add2 = w.count - (wl == first ? 1 : 0)
        let ans = min(add1 + dfs(words, i + 1, first, wl, &memo), add2 + dfs(words, i + 1, wf, last, &memo))
        memo[key] = ans
        return ans
    }
}
