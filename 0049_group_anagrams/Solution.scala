// LeetCode 0049 - Group Anagrams
// https://leetcode.com/problems/group-anagrams/

object Solution {
  def groupAnagrams(strs: Array[String]): List[List[String]] = {
    val groups = scala.collection.mutable.Map[String, scala.collection.mutable.ListBuffer[String]]()

    strs.foreach { word =>
      val key = word.sorted.mkString
      val bucket = groups.getOrElseUpdate(key, scala.collection.mutable.ListBuffer.empty[String])
      bucket += word
    }

    groups.values.map(_.sorted.toList).toList.sortBy(minGroupIndex(strs, _)).reverse
  }

  private def minGroupIndex(strs: Array[String], group: List[String]): Int = {
    group.map(word => strs.indexOf(word)).min
  }
}
