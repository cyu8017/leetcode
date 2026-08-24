// LeetCode 3448 - Count Substrings Divisible By Last Digit
// https://leetcode.com/problems/count-substrings-divisible-by-last-digit/

class Solution {
    func countSubstrings(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var ans = 0
        for r in 0..<n {
            let last = Int(chars[r].asciiValue! - 48)
            if last == 0 { continue }
            var mod = 0
            var p = 1 % last
            for l in stride(from: r, through: 0, by: -1) {
                mod = (mod + Int(chars[l].asciiValue! - 48) * p) % last
                p = (p * 10) % last
                if mod == 0 { ans += 1 }
            }
        }
        return ans
    }
}
