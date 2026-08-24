// LeetCode 0816 - Ambiguous Coordinates
// https://leetcode.com/problems/ambiguous-coordinates/

object Solution {
  def ambiguousCoordinates(s: String): List[String] = {
    val digits = s.substring(1, s.length - 1)
    def candidates(frag: String): List[String] = {
      val options = scala.collection.mutable.ListBuffer.empty[String]
      if (frag.isEmpty || (frag.length > 1 && frag.charAt(0) == '0' && frag.charAt(frag.length - 1) == '0')) {
        return options.toList
      }
      if (frag.charAt(0) == '0' && frag.length > 1) {
        if (frag.charAt(frag.length - 1) != '0') options += ("0." + frag.substring(1))
        return options.toList
      }
      options += frag
      if (frag.charAt(frag.length - 1) == '0') return options.toList
      var i = 1
      while (i < frag.length) {
        options += (frag.substring(0, i) + "." + frag.substring(i))
        i += 1
      }
      options.toList
    }
    val answer = scala.collection.mutable.ListBuffer.empty[String]
    var i = 1
    while (i < digits.length) {
      candidates(digits.substring(0, i)).foreach { left =>
        candidates(digits.substring(i)).foreach { right =>
          answer += s"($left, $right)"
        }
      }
      i += 1
    }
    answer.toList
  }
}
