// LeetCode 0242 - Valid Anagram
// https://leetcode.com/problems/valid-anagram/

class Solution {
    func isAnagram(_ s: String, _ t: String) -> Bool {
        if s.count != t.count {
            return false
        }
        var counts = Array(repeating: 0, count: 26)
        let sChars = Array(s)
        let tChars = Array(t)
        for index in 0..<sChars.count {
            counts[Int(sChars[index].asciiValue! - 97)] += 1
            counts[Int(tChars[index].asciiValue! - 97)] -= 1
        }
        return counts.allSatisfy { $0 == 0 }
    }
}
