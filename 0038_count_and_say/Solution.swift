// LeetCode 0038 - Count and Say
// https://leetcode.com/problems/count-and-say/

class Solution {
    func countAndSay(_ n: Int) -> String {
        var term = "1"

        for _ in 1..<n {
            var nextTerm = ""
            var index = term.startIndex
            while index < term.endIndex {
                var count = 1
                let current = term[index]
                var next = term.index(after: index)
                while next < term.endIndex && term[next] == current {
                    count += 1
                    next = term.index(after: next)
                }
                nextTerm.append(String(count))
                nextTerm.append(current)
                index = next
            }
            term = nextTerm
        }

        return term
    }
}
