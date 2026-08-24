// LeetCode 2575 - Find the Divisibility Array of a String
// https://leetcode.com/problems/find-the-divisibility-array-of-a-string/

class Solution {
    func divisibilityArray(_ word: String, _ m: Int) -> [Int] {
        var ans = [Int](repeating: 0, count: word.count)
        var cur = 0, i = 0
        for ch in word {
            cur = (cur * 10 + Int(ch.asciiValue! - Character("0").asciiValue!)) % m
            if cur == 0 { ans[i] = 1 }
            i += 1
        }
        return ans
    }
}
