// LeetCode 0467 - Unique Substrings in Wraparound String
// https://leetcode.com/problems/unique-substrings-in-wraparound-string/

class Solution {
    func findSubstringInWraproundString(_ s: String) -> Int {
        var counts = Array(repeating: 0, count: 26)
        var length = 0
        let chars = Array(s)

        for index in chars.indices {
            if index > 0 && (Int(chars[index].asciiValue! - chars[index - 1].asciiValue!) + 26) % 26 == 1 {
                length += 1
            } else {
                length = 1
            }
            let position = Int(chars[index].asciiValue! - Character("a").asciiValue!)
            counts[position] = max(counts[position], length)
        }

        return counts.reduce(0, +)
    }
}
