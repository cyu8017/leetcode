// LeetCode 2675 - Array of Objects to Matrix
// https://leetcode.com/problems/array-of-objects-to-matrix/

object Solution {
  def jsonToMatrix(arr: List[scala.collection.mutable.TreeMap[String, String]]): List[List[String]] = {
    val keys = scala.collection.mutable.TreeSet.empty[String]
    arr.foreach(obj => keys ++= obj.keySet)
    val mat = scala.collection.mutable.ArrayBuffer.empty[List[String]]
    mat += keys.toList
    arr.foreach { obj =>
      val row = scala.collection.mutable.ArrayBuffer.empty[String]
      keys.foreach(k => row += obj.getOrElse(k, ""))
      mat += row.toList
    }
    mat.toList
  }
}
