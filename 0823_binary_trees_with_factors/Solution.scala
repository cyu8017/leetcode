// LeetCode 0823 - Binary Trees With Factors
// https://leetcode.com/problems/binary-trees-with-factors/

object Solution {
  def numFactoredBinaryTrees(arr: Array[Int]): Int = {
    val MOD = 1000000007
    scala.util.Sorting.quickSort(arr)
    val dp = scala.collection.mutable.Map.empty[Int, Long]
    var i = 0
    while (i < arr.length) {
      val x = arr(i)
      var ways = 1L
      var j = 0
      while (j < i) {
        val left = arr(j)
        if (x % left == 0) {
          val right = x / left
          if (dp.contains(right)) ways = (ways + dp(left) * dp(right)) % MOD
        }
        j += 1
      }
      dp(x) = ways
      i += 1
    }
    (dp.values.sum % MOD).toInt
  }
}
