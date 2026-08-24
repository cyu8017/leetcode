// LeetCode 2384 - Largest Palindromic Number
// https://leetcode.com/problems/largest-palindromic-number/

class Solution {
    func largestPalindromic(_ num: String) -> String {
        var freq = [Int](repeating: 0, count: 10)
        for c in num { freq[Int(String(c))!] += 1 }
        var left = ""
        for d in stride(from: 9, through: 0, by: -1) {
            let pairs = freq[d] / 2
            left += String(repeating: Character(UnicodeScalar(48 + d)!), count: pairs)
            freq[d] %= 2
        }
        var mid: Character?
        for d in stride(from: 9, through: 0, by: -1) {
            if freq[d] > 0 {
                mid = Character(UnicodeScalar(48 + d)!)
                break
            }
        }
        if left.isEmpty { return mid.map(String.init) ?? "0" }
        if left.first == "0" { return mid.map(String.init) ?? "0" }
        return left + (mid.map(String.init) ?? "") + String(left.reversed())
    }
}
