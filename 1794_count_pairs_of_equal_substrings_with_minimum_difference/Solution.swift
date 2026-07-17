// LeetCode 1794 - Count Pairs of Equal Substrings With Minimum Difference
// https://leetcode.com/problems/count-pairs-of-equal-substrings-with-minimum-difference/

class Solution {
    func countQuadruples(_ firstString: String, _ secondString: String) -> Int {
        let a = Array(firstString.utf8)
        let b = Array(secondString.utf8)
        let base = UInt8(ascii: "a")
        var first = [Int](repeating: -1, count: 26)
        var lastF = [Int](repeating: -1, count: 26)
        var lastS = [Int](repeating: -1, count: 26)
        for (i, ch) in a.enumerated() {
            let c = Int(ch - base)
            if first[c] == -1 { first[c] = i }
            lastF[c] = i
        }
        for (i, ch) in b.enumerated() {
            lastS[Int(ch - base)] = i
        }
        var best = Int.max
        for c in 0..<26 {
            if first[c] != -1 && lastS[c] != -1 {
                best = min(best, lastF[c] - lastS[c])
            }
        }
        if best == Int.max { return 0 }
        var ans = 0
        for c in 0..<26 {
            if first[c] == -1 || lastS[c] == -1 || lastF[c] - lastS[c] != best { continue }
            let ch = base + UInt8(c)
            var iCount = 0
            for k in first[c]...lastF[c] where a[k] == ch { iCount += 1 }
            var aCount = 0
            for k in 0...lastS[c] where b[k] == ch { aCount += 1 }
            ans += iCount * aCount
        }
        return ans
    }
}
