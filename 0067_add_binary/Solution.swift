// LeetCode 0067 - Add Binary
// https://leetcode.com/problems/add-binary/

class Solution {
    func addBinary(_ a: String, _ b: String) -> String {
        var i = a.count - 1
        var j = b.count - 1
        var carry = 0
        var result = ""

        let aChars = Array(a)
        let bChars = Array(b)

        while i >= 0 || j >= 0 || carry != 0 {
            var total = carry
            if i >= 0 {
                total += Int(aChars[i].wholeNumberValue ?? 0)
                i -= 1
            }
            if j >= 0 {
                total += Int(bChars[j].wholeNumberValue ?? 0)
                j -= 1
            }
            result.append(String(total % 2))
            carry = total / 2
        }

        return String(result.reversed())
    }
}
