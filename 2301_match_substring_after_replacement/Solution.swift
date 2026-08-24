// LeetCode 2301 - Match Substring After Replacement
// https://leetcode.com/problems/match-substring-after-replacement/

class Solution {
    func matchReplacement(_ s: String, _ sub: String, _ mappings: [[Character]]) -> Bool {
        var allow = Set<Int>()
        for m in mappings {
            allow.insert((Int(m[0].asciiValue!) << 8) | Int(m[1].asciiValue!))
        }
        let sArr = Array(s), subArr = Array(sub)
        let n = sArr.count, mlen = subArr.count
        if n < mlen { return false }
        for i in 0...(n - mlen) {
            var ok = true
            for j in 0..<mlen {
                let a = sArr[i + j], b = subArr[j]
                if a == b || allow.contains((Int(b.asciiValue!) << 8) | Int(a.asciiValue!)) { continue }
                ok = false
                break
            }
            if ok { return true }
        }
        return false
    }
}
