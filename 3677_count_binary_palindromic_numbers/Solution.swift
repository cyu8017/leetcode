// LeetCode 3677 - Count Binary Palindromic Numbers
// https://leetcode.com/problems/count-binary-palindromic-numbers/

class Solution {
    func countBinaryPalindromes(_ n: Int) -> Int {
        if n == 0 { return 1 }
        var ans = 1
        var bits = [Character]()
        var x = n
        while x > 0 {
            bits.append(Character(UnicodeScalar(48 + (x & 1))!))
            x >>= 1
        }
        let s = Array(bits.reversed())
        let L = s.count
        if L > 1 {
            for len in 1..<L {
                let half = (len + 1) / 2
                ans += 1 << (half - 1)
            }
        }
        let half = (L + 1) / 2
        let prefix = Array(s[0..<half])
        let start = 1 << (half - 1)
        var prefVal = 0
        for c in prefix { prefVal = (prefVal << 1) | Int(c.asciiValue! - 48) }
        ans += prefVal - start
        var pal = prefix
        var i = half - 1 - (L % 2)
        while i >= 0 {
            pal.append(prefix[i])
            i -= 1
        }
        var pval = 0
        for c in pal { pval = (pval << 1) | Int(c.asciiValue! - 48) }
        if pval <= n { ans += 1 }
        return ans
    }
}
