// LeetCode 3734 - Lexicographically Smallest Palindromic Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/

class Solution {
    private var half = [Int]()
    private var left = [Character]()
    private var targetChars = [Character]()
    private var halfLen = 0
    private var mid = -1

    func lexPalindromicPermutation(_ s: String, _ target: String) -> String {
        var cnt = [Int](repeating: 0, count: 26)
        for c in s { cnt[Int(c.asciiValue! - 97)] += 1 }
        var odd = 0
        mid = -1
        for i in 0..<26 {
            if cnt[i] % 2 == 1 { odd += 1; mid = i }
        }
        if odd > 1 { return "" }
        half = [Int](repeating: 0, count: 26)
        for i in 0..<26 { half[i] = cnt[i] / 2 }
        let n = s.count
        halfLen = n / 2
        targetChars = Array(target)
        left = [Character](repeating: "a", count: max(halfLen, 1))
        if !dfs(0, false) { return "" }
        var res = String(left.prefix(halfLen))
        if mid >= 0 { res.append(Character(UnicodeScalar(97 + mid)!)) }
        for i in stride(from: halfLen - 1, through: 0, by: -1) { res.append(left[i]) }
        if res <= target { return "" }
        return res
    }

    private func dfs(_ pos: Int, _ greater: Bool) -> Bool {
        if pos == halfLen {
            if mid >= 0 {
                if greater { return true }
                return Character(UnicodeScalar(97 + mid)!) > targetChars[halfLen]
            }
            return greater
        }
        let start = greater ? 0 : Int(targetChars[pos].asciiValue! - 97)
        for c in start..<26 {
            if half[c] == 0 { continue }
            half[c] -= 1
            left[pos] = Character(UnicodeScalar(97 + c)!)
            if dfs(pos + 1, greater || c > Int(targetChars[pos].asciiValue! - 97)) { return true }
            half[c] += 1
        }
        return false
    }
}
