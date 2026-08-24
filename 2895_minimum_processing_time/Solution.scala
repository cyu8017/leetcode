// LeetCode 2895 - Minimum Processing Time
// https://leetcode.com/problems/minimum-processing-time/

object Solution {
  def minProcessingTime(processorTime: Array[Int], tasks: Array[Int]): Int = {
    val processors = processorTime.sorted
    val t = tasks.sorted(Ordering[Int].reverse)
    var ans = 0
    for (i <- processors.indices) {
      val fin = processors(i) + t(i * 4)
      if (fin > ans) ans = fin
    }
    ans
  }
}
