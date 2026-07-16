// LeetCode 0481 - Magical String
// https://leetcode.com/problems/magical-string/

import scala.collection.mutable

object Solution {
  def magicalString(n: Int): Int = {
    if (n == 0) return 0
    val seq = mutable.ArrayBuffer(1, 2, 2)
    var index = 2
    while (seq.length < n) {
      val next = if (seq.last == 2) 1 else 2
      if (seq(index) == 1) {
        seq += next
      } else {
        seq += next
        if (seq.length < n) seq += next
      }
      index += 1
    }
    seq.take(n).count(_ == 1)
  }
}
