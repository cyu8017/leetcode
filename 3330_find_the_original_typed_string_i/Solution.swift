// LeetCode 3330 - Find the Original Typed String I
// https://leetcode.com/problems/find-the-original-typed-string-i/

class Solution {
    func possibleStringCount(_ word: String) -> Int {
        let w = Array(word)
        var ans = 1
        for i in 1..<w.count where w[i] == w[i - 1] { ans += 1 }
        return ans
    }
}
