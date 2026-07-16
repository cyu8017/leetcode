// LeetCode 0500 - Keyboard Row
// https://leetcode.com/problems/keyboard-row/

class Solution {
    func findWords(_ words: [String]) -> [String] {
        let rows = [
            Set("qwertyuiop"),
            Set("asdfghjkl"),
            Set("zxcvbnm"),
        ]

        func onOneRow(_ word: String) -> Bool {
            let letters = Set(word.lowercased().filter { $0.isLetter })
            return rows.contains { row in
                letters.isSubset(of: row)
            }
        }

        return words.filter(onOneRow)
    }
}
