// LeetCode 2716 - Minimize String Length
// https://leetcode.com/problems/minimize-string-length/

object Solution {
  def minimizedStringLength(s: String): Int = {
    val set = scala.collection.mutable.HashSet.empty[Char]
    var i = 0
    while (i < s.length) {
      set += s.charAt(i)
      i += 1
    }
    set.size
  }
}
