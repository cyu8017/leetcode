// LeetCode 2063 - Vowels of All Substrings
// https://leetcode.com/problems/vowels-of-all-substrings/

class Solution {
    func countVowels(_ word: String) -> Int {
        let chars = Array(word)
        let n = chars.count
        var ans = 0
        for i in 0..<n {
            let c = chars[i]
            if c == "a" || c == "e" || c == "i" || c == "o" || c == "u" {
                ans += (i + 1) * (n - i)
            }
        }
        return ans
    }
}
