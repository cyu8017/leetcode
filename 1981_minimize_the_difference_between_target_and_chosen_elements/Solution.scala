// LeetCode 1981 - Minimize the Difference Between Target and Chosen Elements
// https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/

object Solution {
  def minimizeTheDifference(mat: Array[Array[Int]], target: Int): Int = {
    var possible = Set(0)
    for (row <- mat) {
      val uniq = row.toSet
      val nxt = scala.collection.mutable.Set.empty[Int]
      for (s <- possible; x <- uniq) nxt += s + x
      val kept = nxt.filter(_ <= target).toSet
      val above = nxt.filter(_ > target)
      val nextSet =
        if (above.nonEmpty) kept + above.min
        else if (kept.nonEmpty) kept
        else Set(nxt.min)
      possible = nextSet
    }
    possible.map(v => math.abs(v - target)).min
  }
}
