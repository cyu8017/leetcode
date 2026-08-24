// LeetCode 0784 - Letter Case Permutation
// https://leetcode.com/problems/letter-case-permutation/

class Solution {
    func letterCasePermutation(_ s: String) -> [String] {
        var result = [""]
        for ch in s {
            var next = [String]()
            if ch.isLetter {
                let lower = Character(ch.lowercased())
                let upper = Character(ch.uppercased())
                for prefix in result {
                    next.append(prefix + String(lower))
                    next.append(prefix + String(upper))
                }
            } else {
                for prefix in result { next.append(prefix + String(ch)) }
            }
            result = next
        }
        return result
    }
}
