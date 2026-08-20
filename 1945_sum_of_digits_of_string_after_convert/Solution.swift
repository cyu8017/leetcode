// LeetCode 1945 - Sum of Digits of String After Convert
// https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution {
    func getLucky(_ s: String, _ k: Int) -> Int {
        var num = s.unicodeScalars.map { String(Int($0.value) - 96) }.joined()
        for _ in 0..<k {
            num = String(num.unicodeScalars.reduce(0) { $0 + Int($1.value - 48) })
        }
        return Int(num)!
    }
}
