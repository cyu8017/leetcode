// LeetCode 1370 - Increasing Decreasing String
// https://leetcode.com/problems/increasing-decreasing-string/

class Solution {
    func sortString(_ s: String) -> String {
        var c = Array(repeating: 0, count: 26)
        for ch in s.utf8 { c[Int(ch) - 97] += 1 }
        var out = [Character]()
        while out.count < s.count {
            for i in 0..<26 where c[i] > 0 {
                out.append(Character(UnicodeScalar(97 + i)!)); c[i] -= 1
            }
            for i in stride(from: 25, through: 0, by: -1) where c[i] > 0 {
                out.append(Character(UnicodeScalar(97 + i)!)); c[i] -= 1
            }
        }
        return String(out)
    }
}
