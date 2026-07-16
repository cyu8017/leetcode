// LeetCode 0249 - Group Shifted Strings
// https://leetcode.com/problems/group-shifted-strings/

import scala.collection.mutable

object Solution {
  def groupStrings(strings: Array[String]): List[List[String]] = {
    val groups = mutable.LinkedHashMap.empty[String, mutable.ListBuffer[String]]

    for (text <- strings) {
      val key =
        if (text.isEmpty) {
          ""
        } else {
          val base = text.head
          text.map(ch => ((ch - base + 26) % 26).toString).mkString(",")
        }
      groups.getOrElseUpdate(key, mutable.ListBuffer.empty[String]) += text
    }

    groups.values.map(_.toList).toList
  }
}
