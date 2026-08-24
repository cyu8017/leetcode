// LeetCode 3723 - Maximize Sum Of Squares Of Digits
// https://leetcode.com/problems/maximize-sum-of-squares-of-digits/

class Solution {
    func maxSumOfSquares(_ num: Int, _ sum: Int) -> String {
        if num * 9 < sum { return "" }
        let k = sum / 9, s = sum % 9
        var ans = String(repeating: "9", count: k)
        if s > 0 { ans.append(Character(UnicodeScalar(48 + s)!)) }
        while ans.count < num { ans.append("0") }
        return ans
    }
}
