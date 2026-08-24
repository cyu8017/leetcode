// LeetCode 2531 - Make Number of Distinct Characters Equal
// https://leetcode.com/problems/make-number-of-distinct-characters-equal/

class Solution {
    func isItPossible(_ word1: String, _ word2: String) -> Bool {
        var c1 = [Int](repeating: 0, count: 26)
        var c2 = [Int](repeating: 0, count: 26)
        for c in word1 { c1[Int(c.asciiValue! - Character("a").asciiValue!)] += 1 }
        for c in word2 { c2[Int(c.asciiValue! - Character("a").asciiValue!)] += 1 }
        var d1 = c1.filter { $0 > 0 }.count
        var d2 = c2.filter { $0 > 0 }.count
        for a in 0..<26 where c1[a] > 0 {
            for b in 0..<26 where c2[b] > 0 {
                var nd1 = d1, nd2 = d2
                if a == b {
                    if nd1 == nd2 { return true }
                    continue
                }
                if c1[a] == 1 { nd1 -= 1 }
                if c1[b] == 0 { nd1 += 1 }
                if c2[b] == 1 { nd2 -= 1 }
                if c2[a] == 0 { nd2 += 1 }
                if nd1 == nd2 { return true }
            }
        }
        return false
    }
}
