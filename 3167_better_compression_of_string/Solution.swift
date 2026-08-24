// LeetCode 3167 - Better Compression of String
// https://leetcode.com/problems/better-compression-of-string/

class Solution {
    func betterCompression(_ compressed: String) -> String {
        let chars = Array(compressed)
        var cnt = Array(repeating: 0, count: 26)
        let a = Character("a").asciiValue!
        var i = 0
        while i < chars.count {
            let c = chars[i]
            var j = i + 1, x = 0
            while j < chars.count {
                let d = chars[j]
                guard d >= "0" && d <= "9" else { break }
                x = x * 10 + Int(d.asciiValue! - Character("0").asciiValue!)
                j += 1
            }
            cnt[Int(c.asciiValue! - a)] += x
            i = j
        }
        var ans = ""
        for i in 0..<26 where cnt[i] > 0 {
            ans.append(Character(UnicodeScalar(a + UInt8(i))))
            ans += String(cnt[i])
        }
        return ans
    }
}
