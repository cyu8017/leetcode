// LeetCode 0890 - Find and Replace Pattern
// https://leetcode.com/problems/find-and-replace-pattern/

class Solution {
    func findAndReplacePattern(_ words: [String], _ pattern: String) -> [String] {
        let target = normalize(pattern)
        return words.filter { normalize($0) == target }
    }

    private func normalize(_ s: String) -> [Int] {
        var mapping = [Character: Int]()
        var out = [Int]()
        for ch in s {
            if mapping[ch] == nil { mapping[ch] = mapping.count }
            out.append(mapping[ch]!)
        }
        return out
    }
}
