// LeetCode 0858 - Mirror Reflection
// https://leetcode.com/problems/mirror-reflection/

object Solution {
  def mirrorReflection(p: Int, q: Int): Int = {
    def gcd(a0: Int, b0: Int): Int = {
      var a = a0
      var b = b0
      while (b != 0) {
        val t = a % b
        a = b
        b = t
      }
      a
    }
    var pp = p
    var qq = q
    val g = gcd(pp, qq)
    pp /= g
    qq /= g
    if (pp % 2 == 0) 2
    else if (qq % 2 == 0) 0
    else 1
  }
}
