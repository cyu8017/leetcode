// LeetCode 3750 - Minimum Number Of Flips To Reverse Binary String
// https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string/

class Solution {
    func minimumFlips(_ n: Int) -> Int {
        var x = n
        var s: [Character]
        if x == 0 {
            s = ["0"]
        } else {
            var arr = [Character]()
            while x > 0 {
                arr.append(Character(UnicodeScalar(48 + (x & 1))!))
                x >>= 1
            }
            arr.reverse()
            s = arr
        }
        let m = s.count
        var cnt = 0
        for i in 0..<(m / 2) {
            if s[i] != s[m - i - 1] { cnt += 1 }
        }
        return cnt * 2
    }
}
