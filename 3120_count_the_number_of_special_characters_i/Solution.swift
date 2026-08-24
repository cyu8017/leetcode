// LeetCode 3120 - Count the Number of Special Characters I
// https://leetcode.com/problems/count-the-number-of-special-characters-i/

class Solution {
    func numberOfSpecialChars(_ word: String) -> Int {
        var s = Set<Character>()
        for c in word { s.insert(c) }
        var ans = 0
        let lowers = Array("abcdefghijklmnopqrstuvwxyz")
        let uppers = Array("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        for i in 0..<26 {
            if s.contains(lowers[i]) && s.contains(uppers[i]) { ans += 1 }
        }
        return ans
    }
}
