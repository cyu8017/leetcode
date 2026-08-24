// LeetCode 3121 - Count the Number of Special Characters II
// https://leetcode.com/problems/count-the-number-of-special-characters-ii/

class Solution {
    func numberOfSpecialChars(_ word: String) -> Int {
        var first = Array(repeating: 0, count: 128)
        var last = Array(repeating: 0, count: 128)
        for (i, c) in word.enumerated() {
            let idx = Int(c.asciiValue!)
            if first[idx] == 0 { first[idx] = i + 1 }
            last[idx] = i + 1
        }
        var ans = 0
        for i in 0..<26 {
            let lo = Int(Character("a").asciiValue!) + i
            let up = Int(Character("A").asciiValue!) + i
            if last[lo] > 0 && last[lo] < first[up] { ans += 1 }
        }
        return ans
    }
}
