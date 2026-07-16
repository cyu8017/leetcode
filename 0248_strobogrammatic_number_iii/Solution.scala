// LeetCode 0248 - Strobogrammatic Number III
// https://leetcode.com/problems/strobogrammatic-number-iii/

object Solution {
  private val pairs = Array(
    ("0", "0"),
    ("1", "1"),
    ("6", "9"),
    ("8", "8"),
    ("9", "6"),
  )

  def strobogrammaticInRange(low: String, high: String): Int = {
    val lowValue = BigInt(low)
    val highValue = BigInt(high)
    var count = 0

    for (length <- low.length to high.length) {
      for (value <- build(0, length - 1)) {
        val numeric = BigInt(value)
        if (numeric >= lowValue && numeric <= highValue) {
          count += 1
        }
      }
    }
    count
  }

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
