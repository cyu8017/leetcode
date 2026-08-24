// LeetCode 2942 - Find Words Containing Character
// https://leetcode.com/problems/find-words-containing-character/

class Solution {
    func findWordsContaining(_ words: [String], _ x: Character) -> [Int] {
        var ans: [Int] = []
        for i in 0..<words.count where words[i].contains(x) {
            ans.append(i)
        }
        return ans
    }
}
