// LeetCode 3304 - Find the K-th Character in String Game I
// https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/

class Solution {
    func kthCharacter(_ k: Int) -> Character {
        var s = [Character](["a"])
        while s.count < k {
            let n = s.count
            for i in 0..<n {
                let v = Int(s[i].asciiValue! - 97)
                s.append(Character(UnicodeScalar((v + 1) % 26 + 97)!))
            }
        }
        return s[k - 1]
    }
}
