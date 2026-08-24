// LeetCode 0835 - Image Overlap
// https://leetcode.com/problems/image-overlap/

object Solution {
  def largestOverlap(img1: Array[Array[Int]], img2: Array[Array[Int]]): Int = {
    val n = img1.length
    val ones1 = scala.collection.mutable.ListBuffer.empty[(Int, Int)]
    val ones2 = scala.collection.mutable.ListBuffer.empty[(Int, Int)]
    var i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        if (img1(i)(j) == 1) ones1 += ((i, j))
        if (img2(i)(j) == 1) ones2 += ((i, j))
        j += 1
      }
      i += 1
    }
    if (ones1.isEmpty || ones2.isEmpty) return 0
    val shifts = scala.collection.mutable.Map.empty[Long, Int]
    var best = 0
    ones1.foreach { case (a0, a1) =>
      ones2.foreach { case (b0, b1) =>
        val key = ((a0 - b0 + n).toLong << 16) | (a1 - b1 + n)
        val nxt = shifts.getOrElse(key, 0) + 1
        shifts(key) = nxt
        best = math.max(best, nxt)
      }
    }
    best
  }
}
