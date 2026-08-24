// LeetCode 2075 - Decode the Slanted Ciphertext
// https://leetcode.com/problems/decode-the-slanted-ciphertext/

class Solution {
    fun decodeCiphertext(encodedText: String, rows: Int): String {
if (rows == 1) {
return encodedText
}
var cols: Int = encodedText.length / rows
var b: StringBuilder = StringBuilder()
for (c in 0 until cols) {
for (r in 0 until rows && c + r < cols) {
b.append(encodedText[r * cols + c + r])
}
}
while (b.size > 0 && b[b.length(] - 1) == ' ') {
b.setLength(b.size - 1)
}
return b.toString()
}
}
