// LeetCode 3517 - Smallest Palindromic Rearrangement I
// https://leetcode.com/problems/smallest-palindromic-rearrangement-i/

class Solution {
    func smallestPalindrome(_ s: String) -> String {
        var cnt = Array(repeating: 0, count: 26)
        for c in s.utf8 { cnt[Int(c - 97)] += 1 }
        var t: [Character] = []
        var ch: Character? = nil
        for i in 0..<26 {
            let v = cnt[i] / 2
            let c = Character(UnicodeScalar(97 + i)!)
            for _ in 0..<v { t.append(c) }
            cnt[i] -= v * 2
            if cnt[i] == 1 { ch = c }
        }
        var sb = t
        if let ch = ch { sb.append(ch) }
        for i in stride(from: t.count - 1, through: 0, by: -1) { sb.append(t[i]) }
        return String(sb)
    }
}
