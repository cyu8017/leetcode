// LeetCode 2953 - Count Complete Substrings
// https://leetcode.com/problems/count-complete-substrings/

class Solution {
    func countCompleteSubstrings(_ word: String, _ k: Int) -> Int {
        let chars = Array(word)
        let n = chars.count
        var ans = 0
        var i = 0
        while i < n {
            var j = i
            while j + 1 < n && abs(Int(chars[j + 1].asciiValue!) - Int(chars[j].asciiValue!)) <= 2 {
                j += 1
            }
            let seg = Array(chars[i...j])
            let m = seg.count
            for chCount in 1...26 {
                let length = chCount * k
                if length > m { break }
                var freq = Array(repeating: 0, count: 26)
                var unique = 0
                for r in 0..<m {
                    let c = Int(seg[r].asciiValue! - Character("a").asciiValue!)
                    freq[c] += 1
                    if freq[c] == 1 { unique += 1 }
                    if r >= length {
                        let c2 = Int(seg[r - length].asciiValue! - Character("a").asciiValue!)
                        freq[c2] -= 1
                        if freq[c2] == 0 { unique -= 1 }
                    }
                    if r >= length - 1 && unique == chCount {
                        var ok = true
                        for f in freq where f != 0 && f != k {
                            ok = false
                            break
                        }
                        if ok { ans += 1 }
                    }
                }
            }
            i = j + 1
        }
        return ans
    }
}
