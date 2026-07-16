// LeetCode 0076 - Minimum Window Substring
// https://leetcode.com/problems/minimum-window-substring/

import scala.collection.mutable

object Solution {
  def minWindow(s: String, t: String): String = {
    if (t.isEmpty) {
      return ""
    }

    val need = mutable.Map[Char, Int]().withDefaultValue(0)
    t.foreach { ch =>
      need(ch) += 1
    }

    val required = need.size
    var formed = 0
    val window = mutable.Map[Char, Int]().withDefaultValue(0)
    val chars = s.toArray
    var left = 0
    var bestLen = Int.MaxValue
    var bestLeft = 0

    chars.indices.foreach { right =>
      val ch = chars(right)
      window(ch) += 1
      if (need.contains(ch) && window(ch) == need(ch)) {
        formed += 1
      }

      while (formed == required) {
        if (right - left + 1 < bestLen) {
          bestLen = right - left + 1
          bestLeft = left
        }

        val leftCh = chars(left)
        window(leftCh) -= 1
        if (need.contains(leftCh) && window(leftCh) < need(leftCh)) {
          formed -= 1
        }
        left += 1
      }
    }

    if (bestLen == Int.MaxValue) {
      ""
    } else {
      s.substring(bestLeft, bestLeft + bestLen)
    }
  }
}
