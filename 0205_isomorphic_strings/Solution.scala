// LeetCode 0205 - Isomorphic Strings\n// https://leetcode.com/problems/\n\nimport scala.collection.mutable

object Solution {
  def isIsomorphic(s: String, t: String): Boolean = {
    val forward = mutable.Map[Char, Char]()
    val backward = mutable.Map[Char, Char]()
    for ((a, b) <- s.zip(t)) {
      if (forward.get(a).exists(_ != b) || backward.get(b).exists(_ != a)) return false
      forward(a) = b
      backward(b) = a
    }
    true
  }
}
