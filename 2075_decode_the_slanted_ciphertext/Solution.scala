// LeetCode 2075 - Decode the Slanted Ciphertext
// https://leetcode.com/problems/decode-the-slanted-ciphertext/

object Solution {
  def decodeCiphertext(encodedText: String, rows: Int): String = {
    if (rows == 1) return encodedText
    val cols = encodedText.length / rows
    val b = new StringBuilder
    var c = 0
    while (c < cols) {
      var r = 0
      while (r < rows && c + r < cols) {
        b.append(encodedText.charAt(r * cols + c + r))
        r += 1
      }
      c += 1
    }
    while (b.nonEmpty && b.charAt(b.length - 1) == ' ') b.setLength(b.length - 1)
    b.toString
  }
}
