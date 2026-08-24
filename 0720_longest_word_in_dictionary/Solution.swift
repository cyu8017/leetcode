// LeetCode 0720 - Longest Word in Dictionary
// https://leetcode.com/problems/longest-word-in-dictionary/

class Solution {
    func longestWord(_ words: [String]) -> String {
        let words = words.sorted()
        var built = Set<String>([""])
        var best = ""
        for word in words {
            if built.contains(String(word.dropLast())) {
                built.insert(word)
                if word.count > best.count { best = word }
            }
        }
        return best
    }
}
