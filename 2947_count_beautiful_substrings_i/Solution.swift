// LeetCode 2947 - Count Beautiful Substrings I
// https://leetcode.com/problems/count-beautiful-substrings-i/

class Solution {
    func beautifulSubstrings(_ s: String, _ k: Int) -> Int {
        let chars = Array(s)
        var ans = 0
        for i in 0..<chars.count {
            var v = 0, c = 0
            for j in i..<chars.count {
                if isVowel(chars[j]) { v += 1 }
                else { c += 1 }
                if v == c && (v * c) % k == 0 { ans += 1 }
            }
        }
        return ans
    }

    private func isVowel(_ ch: Character) -> Bool {
        return ch == "a" || ch == "e" || ch == "i" || ch == "o" || ch == "u"
    }
}
