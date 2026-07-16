// LeetCode 0301 - Remove Invalid Parentheses
// https://leetcode.com/problems/remove-invalid-parentheses/

class Solution {
    func removeInvalidParentheses(_ s: String) -> [String] {
        func isValid(_ text: String) -> Bool {
            var balance = 0
            for char in text {
                if char == "(" {
                    balance += 1
                } else if char == ")" {
                    if balance == 0 {
                        return false
                    }
                    balance -= 1
                }
            }
            return balance == 0
        }

        var result = Set<String>()
        var queue = [s]
        var visited = Set<String>([s])
        var found = false
        while !queue.isEmpty {
            let levelSize = queue.count
            for _ in 0..<levelSize {
                let current = queue.removeFirst()
                if isValid(current) {
                    result.insert(current)
                    found = true
                }
                if found {
                    continue
                }
                let chars = Array(current)
                for index in 0..<chars.count {
                    if chars[index] != "(" && chars[index] != ")" {
                        continue
                    }
                    var nextChars = chars
                    nextChars.remove(at: index)
                    let next = String(nextChars)
                    if visited.contains(next) {
                        continue
                    }
                    visited.insert(next)
                    queue.append(next)
                }
            }
        }
        return Array(result)
    }
}
