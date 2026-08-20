// LeetCode 1585 - Check If String Is Transformable With Substring Sort Operations
// https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/

class Solution {
    func isTransformable(_ s: String, _ t: String) -> Bool {
        var positions = Array(repeating: [Int](), count: 10)
        for (i, ch) in s.enumerated() {
            positions[Int(String(ch))!].append(i)
        }
        var heads = Array(repeating: 0, count: 10)
        for ch in t {
            let d = Int(String(ch))!
            if heads[d] >= positions[d].count { return false }
            let index = positions[d][heads[d]]
            for smaller in 0..<d {
                if heads[smaller] < positions[smaller].count && positions[smaller][heads[smaller]] < index {
                    return false
                }
            }
            heads[d] += 1
        }
        return true
    }
}
