// LeetCode 1081 - Smallest Subsequence of Distinct Characters
// https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

class Solution {
    func smallestSubsequence(_ s: String) -> String {
        let chars = Array(s)
        var last: [Character: Int] = [:]
        for (i, ch) in chars.enumerated() {
            last[ch] = i
        }
        var stack: [Character] = []
        var used = Set<Character>()
        for (i, ch) in chars.enumerated() {
            if used.contains(ch) { continue }
            while let top = stack.last, ch < top, last[top]! > i {
                used.remove(stack.removeLast())
            }
            stack.append(ch)
            used.insert(ch)
        }
        return String(stack)
    }
}
