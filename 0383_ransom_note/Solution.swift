// LeetCode 0383 - Ransom Note
// https://leetcode.com/problems/ransom-note/

class Solution {
    func canConstruct(_ ransomNote: String, _ magazine: String) -> Bool {
        var counts: [Character: Int] = [:]
        for char in magazine {
            counts[char, default: 0] += 1
        }

        for char in ransomNote {
            guard let remaining = counts[char], remaining > 0 else {
                return false
            }
            counts[char] = remaining - 1
        }

        return true
    }
}
