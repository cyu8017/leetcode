// LeetCode 0071 - Simplify Path
// https://leetcode.com/problems/simplify-path/

class Solution {
    func simplifyPath(_ path: String) -> String {
        var stack: [String] = []

        for part in path.split(separator: "/", omittingEmptySubsequences: false) {
            let token = String(part)
            if token.isEmpty || token == "." {
                continue
            }
            if token == ".." {
                if !stack.isEmpty {
                    stack.removeLast()
                }
            } else {
                stack.append(token)
            }
        }

        return "/" + stack.joined(separator: "/")
    }
}
