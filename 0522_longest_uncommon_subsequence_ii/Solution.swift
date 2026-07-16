// LeetCode 0522 - Longest Uncommon Subsequence II
// https://leetcode.com/problems/longest-uncommon-subsequence-ii/

class Solution {
    func findLUSlength(_ strs: [String]) -> Int {
        var result = -1
        for i in 0..<strs.count {
            let candidate = strs[i]
            if strs.enumerated().contains(where: { j, other in
                i != j && isSubsequence(candidate, other)
            }) {
                continue
            }
            result = max(result, candidate.count)
        }
        return result
    }

    private func isSubsequence(_ target: String, _ source: String) -> Bool {
        var index = target.startIndex
        for char in source {
            if index < target.endIndex && target[index] == char {
                index = target.index(after: index)
            }
        }
        return index == target.endIndex
    }
}
