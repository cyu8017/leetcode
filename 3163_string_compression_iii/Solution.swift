// LeetCode 3163 - String Compression III
// https://leetcode.com/problems/string-compression-iii/

class Solution {
    func compressedString(_ word: String) -> String {
        let chars = Array(word)
        var ans = ""
        var i = 0
        while i < chars.count {
            var j = i + 1
            while j < chars.count && chars[j] == chars[i] { j += 1 }
            var k = j - i
            while k > 0 {
                let x = min(9, k)
                ans.append(Character(UnicodeScalar(UInt8(Character("0").asciiValue!) + UInt8(x))))
                ans.append(chars[i])
                k -= x
            }
            i = j
        }
        return ans
    }
}
