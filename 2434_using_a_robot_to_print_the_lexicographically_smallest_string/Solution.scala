// LeetCode 2434 - Using a Robot to Print the Lexicographically Smallest String
// https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

object Solution {
  def robotWithString(s: String): String = {
    val n = s.length
    val minSuf = new Array[Char](n + 1)
    minSuf(n) = ('z' + 1).toChar
    var i = n - 1
    while (i >= 0) {
      minSuf(i) = if (s.charAt(i) < minSuf(i + 1)) s.charAt(i) else minSuf(i + 1)
      i -= 1
    }
    val stack = new StringBuilder()
    val ans = new StringBuilder()
    i = 0
    while (i < n) {
      stack.append(s.charAt(i))
      while (stack.length > 0 && stack.charAt(stack.length - 1) <= minSuf(i + 1)) {
        ans.append(stack.charAt(stack.length - 1))
        stack.setLength(stack.length - 1)
      }
      i += 1
    }
    while (stack.length > 0) {
      ans.append(stack.charAt(stack.length - 1))
      stack.setLength(stack.length - 1)
    }
    ans.toString
  }
}
