// LeetCode 0247 - Strobogrammatic Number II
// https://leetcode.com/problems/strobogrammatic-number-ii/

object Solution {
  private val pairs = Array(
    ("0", "0"),
    ("1", "1"),
    ("6", "9"),
    ("8", "8"),
    ("9", "6"),
  )

  def findStrobogrammatic(n: Int): List[String] = build(0, n - 1)

  private def build(left: Int, right: Int): List[String] = {
    if (left > right) {
      List("")
    } else if (left == right) {
      List("0", "1", "8")
    } else {
      pairs.flatMap { case (start, end) =>
        if (left == 0 && start == "0") {
          Nil
        } else {
          build(left + 1, right - 1).map(middle => start + middle + end)
        }
      }
    }
  }
}
