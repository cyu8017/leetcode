// LeetCode 3407 - Substring Matching Pattern
// https://leetcode.com/problems/substring-matching-pattern/

class Solution {
    func hasMatch(_ s: String, _ p: String) -> Bool {
        let pa = Array(p)
        let star = pa.firstIndex(of: "*")!
        let left = String(pa[..<star])
        let right = String(pa[(star + 1)...])
        guard let li = s.range(of: left) else { return false }
        let rest = s[li.upperBound...]
        return rest.range(of: right) != nil
    }
}
