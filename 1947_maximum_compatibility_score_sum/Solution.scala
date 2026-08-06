// LeetCode 1947 - Maximum Compatibility Score Sum
// https://leetcode.com/problems/maximum-compatibility-score-sum/

object Solution {
  def maxCompatibilitySum(students: Array[Array[Int]], mentors: Array[Array[Int]]): Int = {
    val m = students.length
    val score = Array.ofDim[Int](m, m)
    for (i <- 0 until m; j <- 0 until m) {
      score(i)(j) = students(i).indices.count(k => students(i)(k) == mentors(j)(k))
    }
    val memo = scala.collection.mutable.Map.empty[(Int, Int), Int]
    def dp(i: Int, mask: Int): Int = {
      if (i == m) return 0
      memo.getOrElseUpdate((i, mask), {
        var best = 0
        for (j <- 0 until m if (mask & (1 << j)) == 0) {
          best = math.max(best, score(i)(j) + dp(i + 1, mask | (1 << j)))
        }
        best
      })
    }
    dp(0, 0)
  }
}
