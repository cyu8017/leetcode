// LeetCode 3138 - Minimum Length of Anagram Concatenation
// https://leetcode.com/problems/minimum-length-of-anagram-concatenation/

class Solution {
    func minAnagramLength(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var cnt = Array(repeating: 0, count: 26)
        let a = Character("a").asciiValue!
        for c in chars { cnt[Int(c.asciiValue! - a)] += 1 }
        var i = 1
        while true {
            if n % i == 0 && check(chars, n, cnt, i) { return i }
            i += 1
        }
    }

    private func check(_ s: [Character], _ n: Int, _ cnt: [Int], _ k: Int) -> Bool {
        let a = Character("a").asciiValue!
        var i = 0
        while i < n {
            var cnt1 = Array(repeating: 0, count: 26)
            for j in i..<(i + k) { cnt1[Int(s[j].asciiValue! - a)] += 1 }
            for j in 0..<26 {
                if cnt1[j] * (n / k) != cnt[j] { return false }
            }
            i += k
        }
        return true
    }
}
