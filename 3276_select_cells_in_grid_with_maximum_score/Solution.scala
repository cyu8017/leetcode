// LeetCode 3276 - Select Cells in Grid With Maximum Score
// https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/

object Solution {
  def maxScore(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val vals = scala.collection.mutable.HashMap.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]
    var i = 0
    while (i < m) {
      val seen = scala.collection.mutable.HashSet.empty[Int]
      for (v <- grid(i)) {
        if (seen.add(v)) {
          if (!vals.contains(v)) vals(v) = scala.collection.mutable.ArrayBuffer.empty[Int]
          vals(v) += i
        }
      }
      i += 1
    }
    val arr = vals.keys.toArray.sorted.reverse
    val N = 1 << m
    var dp = new Array[Int](N)
    for (v <- arr) {
      val ndp = dp.clone()
      for (r <- vals(v)) {
        val bit = 1 << r
        var mask = 0
        while (mask < N) {
          if ((mask & bit) == 0) {
            val cand = dp(mask) + v
            val nmask = mask | bit
            if (cand > ndp(nmask)) ndp(nmask) = cand
          }
          mask += 1
        }
      }
      dp = ndp
    }
    var ans = 0
    for (x <- dp) ans = math.max(ans, x)
    ans
  }
}
