// LeetCode 0168 - Excel Sheet Column Title
// https://leetcode.com/problems/excel-sheet-column-title/

class Solution {
    func convertToTitle(_ columnNumber: Int) -> String {
        var number = columnNumber
        var chars = [Character]()
        while number > 0 {
            number -= 1
            chars.append(Character(UnicodeScalar(UInt8(65 + number % 26))))
            number /= 26
        }
        return String(chars.reversed())
    }
}