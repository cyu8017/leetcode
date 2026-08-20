// LeetCode 1400 - Construct K Palindrome Strings
// https://leetcode.com/problems/construct-k-palindrome-strings/

class Solution {
    func canConstruct(_ s: String, _ k: Int) -> Bool {
        var c = [Character: Int]()
        for ch in s { c[ch, default: 0] += 1 }
        let odd = c.values.filter { $0 % 2 != 0 }.count
        return odd <= k && k <= s.count
    }
}
