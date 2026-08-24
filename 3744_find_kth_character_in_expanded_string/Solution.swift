// LeetCode 3744 - Find Kth Character in Expanded String
// https://leetcode.com/problems/find-kth-character-in-expanded-string/

class Solution {
    func kthCharacter(_ s: String, _ k: Int) -> Character {
        var k = k
        let words = s.split { $0.isWhitespace }.map(String.init)
        for w in words {
            let chars = Array(w)
            let m = (1 + chars.count) * chars.count / 2
            if k == m { return " " }
            if k > m {
                k -= m + 1
            } else {
                var cur = 0
                var i = 0
                while true {
                    cur += i + 1
                    if k < cur { return chars[i] }
                    i += 1
                }
            }
        }
        return " "
    }
}
