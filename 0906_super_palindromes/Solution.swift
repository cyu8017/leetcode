// LeetCode 0906 - Super Palindromes
// https://leetcode.com/problems/super-palindromes/

class Solution {
    func superpalindromesInRange(_ left: String, _ right: String) -> Int {
        let L = Int(left)!, R = Int(right)!
        var ans = 0
        func isPal(_ x: Int) -> Bool {
            let s = Array(String(x))
            return s == s.reversed()
        }
        for k in 1...100000 {
            let s = String(k)
            let pal = Int(s + String(s.reversed()))!
            let sq = pal * pal
            if sq > R { break }
            if sq >= L && isPal(sq) { ans += 1 }
        }
        for k in 1...100000 {
            let s = Array(String(k))
            var palChars = s
            if s.count > 1 {
                palChars += s.dropLast().reversed()
            }
            let pal = Int(String(palChars))!
            let sq = pal * pal
            if sq > R { break }
            if sq >= L && isPal(sq) { ans += 1 }
        }
        return ans
    }
}
