// LeetCode 3838 - Weighted Word Mapping
// https://leetcode.com/problems/weighted-word-mapping/

class Solution {
    func mapWordWeights(_ words: [String], _ weights: [Int]) -> String {
        var ans = ""
        for w in words {
            var s = 0
            for c in w { s = (s + weights[Int(c.asciiValue! - 97)]) % 26 }
            ans.append(Character(UnicodeScalar(97 + (25 - s))!))
        }
        return ans
    }
}
