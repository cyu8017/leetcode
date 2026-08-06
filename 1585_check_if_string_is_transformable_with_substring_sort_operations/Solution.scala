// LeetCode 1585 - Check If String Is Transformable With Substring Sort Operations
// https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/

object Solution {
  def isTransformable(s: String, t: String): Boolean = {
    val positions = Array.fill(10)(scala.collection.mutable.Queue.empty[Int])
    for (i <- s.indices) positions(s(i) - '0').enqueue(i)
    for (ch <- t) {
      val d = ch - '0'
      if (positions(d).isEmpty) return false
      val index = positions(d).front
      if ((0 until d).exists(smaller => positions(smaller).nonEmpty && positions(smaller).front < index)) return false
      positions(d).dequeue()
    }
    true
  }
}
