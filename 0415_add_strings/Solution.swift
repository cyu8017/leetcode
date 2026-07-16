// LeetCode 0415 - Add Strings
// https://leetcode.com/problems/add-strings/

class Solution {
    func addStrings(_ num1: String, _ num2: String) -> String {
        var index1 = num1.count - 1
        var index2 = num2.count - 1
        var carry = 0
        var digits: [Character] = []
        let chars1 = Array(num1)
        let chars2 = Array(num2)

        while index1 >= 0 || index2 >= 0 || carry > 0 {
            if index1 >= 0 {
                carry += Int(String(chars1[index1]))!
                index1 -= 1
            }
            if index2 >= 0 {
                carry += Int(String(chars2[index2]))!
                index2 -= 1
            }
            digits.append(Character(String(carry % 10)))
            carry /= 10
        }

        return String(digits.reversed())
    }
}
