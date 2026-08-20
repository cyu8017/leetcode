// LeetCode 1156 - Swap For Longest Repeated Character Substring
// https://leetcode.com/problems/swap-for-longest-repeated-character-substring/

class Solution {
    func maxRepOpt1(_ text: String) -> Int {
        let chars = Array(text)
        var count = [Int](repeating: 0, count: 26)
        for ch in chars {
            count[Int(ch.asciiValue! - 97)] += 1
        }
        let n = chars.count
        var ans = 0, i = 0
        while i < n {
            var j = i
            while j < n && chars[j] == chars[i] { j += 1 }
            let length = j - i
            var k = j + 1
            while k < n && chars[k] == chars[i] { k += 1 }
            let length2 = j < n ? k - j - 1 : 0
            ans = max(ans, min(length + length2 + 1, count[Int(chars[i].asciiValue! - 97)]))
            i = j
        }
        return ans
    }
}
