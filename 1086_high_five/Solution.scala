// LeetCode 1086 - High Five
// https://leetcode.com/problems/high-five/

object Solution {
  def highFive(items: Array[Array[Int]]): Array[Array[Int]] = {
    val scores = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]
    for (item <- items) {
      val id = item(0)
      val score = item(1)
      if (!scores.contains(id)) scores(id) = scala.collection.mutable.ArrayBuffer.empty[Int]
      scores(id) += score
    }
    scores.keys.toArray.sorted.map { id =>
      val top = scores(id).sorted.reverse.take(5)
      Array(id, top.sum / 5)
    }
  }
}
