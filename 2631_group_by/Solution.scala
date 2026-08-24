// LeetCode 2631 - Group By
// https://leetcode.com/problems/group-by/

object Solution {
  def groupBy(arr: Array[Int], fn: Int => String): Map[String, List[Int]] = {
    val out = scala.collection.mutable.LinkedHashMap.empty[String, scala.collection.mutable.ArrayBuffer[Int]]
    var i = 0
    while (i < arr.length) {
      val k = fn(arr(i))
      out.getOrElseUpdate(k, scala.collection.mutable.ArrayBuffer.empty[Int]) += arr(i)
      i += 1
    }
    out.map { case (k, v) => k -> v.toList }.toMap
  }
}
