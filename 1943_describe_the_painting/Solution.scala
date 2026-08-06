// LeetCode 1943 - Describe the Painting
// https://leetcode.com/problems/describe-the-painting/

object Solution {
  def splitPainting(segments: Array[Array[Int]]): List[List[Long]] = {
    val diff = scala.collection.mutable.Map.empty[Int, Long].withDefaultValue(0L)
    for (seg <- segments) {
      diff(seg(0)) += seg(2)
      diff(seg(1)) -= seg(2)
    }
    val points = diff.keys.toArray.sorted
    val ans = scala.collection.mutable.ListBuffer.empty[List[Long]]
    var cur = 0L
    for (i <- 0 until points.length - 1) {
      cur += diff(points(i))
      if (cur != 0) ans += List(points(i).toLong, points(i + 1).toLong, cur)
    }
    ans.toList
  }
}
