// LeetCode 0171 - Excel Sheet Column Number
// https://leetcode.com/problems/excel-sheet-column-number/

class Solution {
    func titleToNumber(_ columnTitle: String) -> Int {
        var result = 0
        for scalar in columnTitle.unicodeScalars {
            result = result * 26 + Int(scalar.value - 64)
        }
        return result
    }
}