// LeetCode 2722 - Join Two Arrays by ID
// https://leetcode.com/problems/join-two-arrays-by-id/

object Solution {
  def join(
    arr1: List[scala.collection.mutable.TreeMap[String, Int]],
    arr2: List[scala.collection.mutable.TreeMap[String, Int]]
  ): List[scala.collection.mutable.TreeMap[String, Int]] = {
    val byId = scala.collection.mutable.TreeMap.empty[Int, scala.collection.mutable.TreeMap[String, Int]]
    merge(byId, arr1)
    merge(byId, arr2)
    byId.values.toList
  }

  private def merge(
    byId: scala.collection.mutable.TreeMap[Int, scala.collection.mutable.TreeMap[String, Int]],
    arr: List[scala.collection.mutable.TreeMap[String, Int]]
  ): Unit = {
    arr.foreach { obj =>
      val id = obj("id")
      val dest = byId.getOrElseUpdate(id, scala.collection.mutable.TreeMap.empty[String, Int])
      dest ++= obj
    }
  }
}
