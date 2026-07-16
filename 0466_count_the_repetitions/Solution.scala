// LeetCode 0466 - Count The Repetitions
// https://leetcode.com/problems/count-the-repetitions/

import scala.collection.mutable

object Solution {
  def getMaxRepetitions(s1: String, n1: Int, s2: String, n2: Int): Int = {
    if (s2.isEmpty) {
      return 0
    }

    val chars1 = s1.toCharArray
    val chars2 = s2.toCharArray
    var index = 0
    var s2Count = 0
    val record = mutable.Map.empty[Int, (Int, Int)]

    var repeatIndex = 0
    while (repeatIndex < n1) {
      var position = 0
      while (position < chars1.length) {
        if (chars1(position) == chars2(index)) {
          index += 1
          if (index == chars2.length) {
            index = 0
            s2Count += 1
          }
        }
        position += 1
      }

      record.get(index) match {
        case Some((previousRepeat, previousCount)) =>
          val cycle = repeatIndex - previousRepeat
          val countCycle = s2Count - previousCount
          val remaining = n1 - repeatIndex - 1
          s2Count += (remaining / cycle) * countCycle
          if (repeatIndex + (remaining / cycle) * cycle >= n1 - 1) {
            return s2Count / n2
          }
        case None =>
      }
      record(index) = (repeatIndex, s2Count)
      repeatIndex += 1
    }

    s2Count / n2
  }
}
