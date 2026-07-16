// LeetCode 0022 - Generate Parentheses
// https://leetcode.com/problems/generate-parentheses/

class Solution {
    func generateParenthesis(_ n: Int) -> [String] {
        var result: [String] = []
        var path: [Character] = []

        func backtrack(_ openCount: Int, _ closeCount: Int) {
            if path.count == 2 * n {
                result.append(String(path))
                return
            }
            if openCount < n {
                path.append("(")
                backtrack(openCount + 1, closeCount)
                path.removeLast()
            }
            if closeCount < openCount {
                path.append(")")
                backtrack(openCount, closeCount + 1)
                path.removeLast()
            }
        }

        backtrack(0, 0)
        return result
    }
}
