// LeetCode 0320 - Generalized Abbreviation
// https://leetcode.com/problems/generalized-abbreviation/

class Solution {
    func generateAbbreviations(_ word: String) -> [String] {
        var result: [String] = []
        let chars = Array(word)

        func backtrack(_ index: Int, _ path: String, _ count: Int) {
            if index == chars.count {
                result.append(path + (count == 0 ? "" : String(count)))
                return
            }
            backtrack(index + 1, path, count + 1)
            let nextPath = path + (count == 0 ? "" : String(count)) + String(chars[index])
            backtrack(index + 1, nextPath, 0)
        }

        backtrack(0, "", 0)
        return result
    }
}
