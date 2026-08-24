// LeetCode 2949 - Count Beautiful Substrings II
// https://leetcode.com/problems/count-beautiful-substrings-ii/

class Solution {
    func beautifulSubstrings(_ s: String, _ k: Int) -> Int {
        var x = 1
        while (x * x) % k != 0 { x += 1 }
        var freq: [Int: Int] = [0: 1]
        var bal = 0, vowels = 0, ans = 0
        for ch in s {
            if isVowel(ch) {
                bal += 1
                vowels += 1
            } else {
                bal -= 1
            }
            let kk = (bal << 32) | (vowels % x)
            let f = freq[kk, default: 0]
            ans += f
            freq[kk] = f + 1
        }
        return ans
    }

    private func isVowel(_ ch: Character) -> Bool {
        return ch == "a" || ch == "e" || ch == "i" || ch == "o" || ch == "u"
    }
}
