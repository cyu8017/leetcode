// LeetCode 0648 - Replace Words
// https://leetcode.com/problems/replace-words/

class Solution {
    func replaceWords(_ dictionary: [String], _ sentence: String) -> String {
        let roots = Set(dictionary)
        let words = sentence.split(separator: " ").map(String.init)
        return words.map { word in
            for i in 1...word.count {
                let prefix = String(word.prefix(i))
                if roots.contains(prefix) { return prefix }
            }
            return word
        }.joined(separator: " ")
    }
}
