// LeetCode 1065 - Index Pairs of a String
// https://leetcode.com/problems/index-pairs-of-a-string/

class Solution {
    func indexPairs(_ text: String, _ words: [String]) -> [[Int]] {
        let wordSet = Set(words)
        let chars = Array(text)
        var ans: [[Int]] = []
        let n = chars.count
        for i in 0..<n {
            for j in i..<n {
                if wordSet.contains(String(chars[i...j])) {
                    ans.append([i, j])
                }
            }
        }
        return ans
    }
}
