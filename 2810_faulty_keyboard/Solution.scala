// LeetCode 2810 - Faulty Keyboard
// https://leetcode.com/problems/faulty-keyboard/

object Solution {
  def finalString(s: String): String = {
    val b = new StringBuilder
    s.foreach { c =>
      if (c == 'i') {
        val t = b.toString.reverse
        b.clear()
        b.append(t)
      } else b.append(c)
    }
    b.toString
  }
}
