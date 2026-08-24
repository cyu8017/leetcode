// LeetCode 2075 - Decode the Slanted Ciphertext
// https://leetcode.com/problems/decode-the-slanted-ciphertext/

class Solution {
    func decodeCiphertext(_ encodedText: String, _ rows: Int) -> String {
        if rows == 1 { return encodedText }
        let chars = Array(encodedText)
        let cols = chars.count / rows
        var b = [Character]()
        for c in 0..<cols {
            var r = 0
            while r < rows && c + r < cols {
                b.append(chars[r * cols + c + r])
                r += 1
            }
        }
        while !b.isEmpty && b.last == " " { b.removeLast() }
        return String(b)
    }
}
