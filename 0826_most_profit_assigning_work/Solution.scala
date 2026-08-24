// LeetCode 0826 - Most Profit Assigning Work
// https://leetcode.com/problems/most-profit-assigning-work/

object Solution {
  def maxProfitAssignment(difficulty: Array[Int], profit: Array[Int], worker: Array[Int]): Int = {
    val m = difficulty.length
    val jobs = Array.tabulate(m)(i => (difficulty(i), profit(i)))
    scala.util.Sorting.quickSort(jobs)(Ordering.by(_._1))
    scala.util.Sorting.quickSort(worker)
    var ans = 0
    var best = 0
    var i = 0
    worker.foreach { ability =>
      while (i < m && jobs(i)._1 <= ability) {
        best = math.max(best, jobs(i)._2)
        i += 1
      }
      ans += best
    }
    ans
  }
}
