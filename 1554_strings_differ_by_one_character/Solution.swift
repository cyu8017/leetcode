// LeetCode 1554 - Strings Differ by One Character
// https://leetcode.com/problems/strings-differ-by-one-character/

class Solution {
    func differByOne(_ dict: [String]) -> Bool {
        var seen = Set<String>()
        for word in dict {
            let chars = Array(word)
            for i in 0..<chars.count {
                var pattern = chars
                pattern[i] = "*"
                let key = String(pattern)
                if seen.contains(key) { return true }
                seen.insert(key)
            }
        }
        return false
    }
}
