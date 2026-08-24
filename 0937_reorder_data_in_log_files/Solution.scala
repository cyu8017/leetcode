// LeetCode 0937 - Reorder Data in Log Files
// https://leetcode.com/problems/reorder-data-in-log-files/

object Solution {
  def reorderLogFiles(logs: Array[String]): Array[String] = {
    val letter = scala.collection.mutable.ArrayBuffer[String]()
    val digit = scala.collection.mutable.ArrayBuffer[String]()
    logs.foreach { log =>
      val sp = log.indexOf(' ')
      if (log.charAt(sp + 1).isLetter) letter += log
      else digit += log
    }
    val sorted = letter.sortBy { a =>
      val spa = a.indexOf(' ')
      (a.substring(spa + 1), a.substring(0, spa))
    }
    (sorted ++ digit).toArray
  }
}
