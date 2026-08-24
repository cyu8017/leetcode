// LeetCode 2691 - Immutability Helper
// https://leetcode.com/problems/immutability-helper/

object Solution {
  def immutableHelper(
    obj: scala.collection.mutable.TreeMap[String, Int],
    mutators: List[scala.collection.mutable.TreeMap[String, Int] => Unit]
  ): List[scala.collection.mutable.TreeMap[String, Int]] = {
    val out = scala.collection.mutable.ArrayBuffer.empty[scala.collection.mutable.TreeMap[String, Int]]
    mutators.foreach { m =>
      val copy = scala.collection.mutable.TreeMap.empty[String, Int] ++ obj
      m(copy)
      out += copy
    }
    out.toList
  }
}
