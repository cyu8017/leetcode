// LeetCode 0316 - Remove Duplicate Letters
// https://leetcode.com/problems/remove-duplicate-letters/

class Solution {
    func removeDuplicateLetters(_ s: String) -> String {
        let chars = Array(s)
        var lastIndex: [Character: Int] = [:]
        for index in 0..<chars.count {
            lastIndex[chars[index]] = index
        }

        var stack: [Character] = []
        var seen: Set<Character> = []
        for index in 0..<chars.count {
            let char = chars[index]
            if seen.contains(char) {
                continue
            }
            while let last = stack.last,
                  last > char,
                  lastIndex[last]! > index {
                seen.remove(stack.removeLast())
            }
            stack.append(char)
            seen.insert(char)
        }
        return String(stack)
    }
}
