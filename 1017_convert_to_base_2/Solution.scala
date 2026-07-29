// LeetCode 1017 - Convert to Base -2
// https://leetcode.com/problems/convert-to-base-2/

object Solution {
  def baseNeg2(n: Int): String = {
    if (n == 0) return "0"
    val ans = scala.collection.mutable.ArrayBuffer.empty[Char]
    var cur = n
    while (cur != 0) {
      var rem = cur % -2
      cur = cur / -2
      if (rem < 0) {
        cur += 1
        rem += 2
      }
      ans += (rem + '0').toChar
    }
    ans.reverse.mkString
  }
}
