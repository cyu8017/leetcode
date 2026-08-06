// LeetCode 1504 - Count Submatrices With All Ones
// https://leetcode.com/problems/count-submatrices-with-all-ones/

object Solution {
  def numSubmat(mat: Array[Array[Int]]): Int = {
    var ans = 0
    val heights = Array.fill(mat(0).length)(0)
    for (row <- mat) {
      for (j <- row.indices) heights(j) = if (row(j) == 0) 0 else heights(j) + 1
      val stack = scala.collection.mutable.ArrayBuffer.empty[(Int, Int)]
      var running = 0
      for (h <- heights) {
        var count = 1
        while (stack.nonEmpty && stack.last._1 >= h) {
          val (old, width) = stack.remove(stack.length - 1)
          running -= old * width
          count += width
        }
        stack += ((h, count))
        running += h * count
        ans += running
      }
    }
    ans
  }
}
