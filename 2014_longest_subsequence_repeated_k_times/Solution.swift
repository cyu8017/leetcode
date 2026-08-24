// LeetCode 2014 - Longest Subsequence Repeated K Times
// https://leetcode.com/problems/longest-subsequence-repeated-k-times/

class Solution {
    func longestSubsequenceRepeatedK(_ s: String, _ k: Int) -> String {
        let chars = Array(s)
        var freq = [Int](repeating: 0, count: 26)
        for c in chars { freq[Int(c.asciiValue! - 97)] += 1 }
        var usable = [Character]()
        for c in stride(from: 25, through: 0, by: -1) where freq[c] >= k {
            usable.append(Character(UnicodeScalar(97 + c)!))
        }
        var best = ""
        var q = [""]
        var head = 0
        while head < q.count {
            let cur = q[head]
            head += 1
            for ch in usable {
                let nxt = cur + String(ch)
                if isSubseq(chars, Array(nxt), k) {
                    if nxt.count > best.count || (nxt.count == best.count && nxt > best) {
                        best = nxt
                    }
                    q.append(nxt)
                }
            }
        }
        return best
    }

    private func isSubseq(_ s: [Character], _ t: [Character], _ k: Int) -> Bool {
        var need = 0, times = 0
        for ch in s {
            if ch == t[need] {
                need += 1
                if need == t.count {
                    times += 1
                    if times == k { return true }
                    need = 0
                }
            }
        }
        return false
    }
}
