// LeetCode 2700 - Differences Between Two Objects
// https://leetcode.com/problems/differences-between-two-objects/

object Solution {
  def objDiff(
    obj1: scala.collection.mutable.TreeMap[String, Int],
    obj2: scala.collection.mutable.TreeMap[String, Int]
  ): scala.collection.mutable.TreeMap[String, Array[Int]] = {
    val diff = scala.collection.mutable.TreeMap.empty[String, Array[Int]]
    obj1.foreach { case (k, v) =>
      obj2.get(k) match {
        case Some(v2) if v2 != v => diff(k) = Array(v, v2)
        case _ =>
      }
    }
    diff
  }
}
