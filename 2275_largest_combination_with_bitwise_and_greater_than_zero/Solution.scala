// LeetCode 2275 - Largest Combination With Bitwise AND Greater Than Zero
// https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/

object Solution {
  def largestCombination(candidates: Array[Int]): Int = {
    var ans = 0
    var bit = 0
    while (bit < 24) {
      var cnt = 0
      for (x <- candidates) if (((x >> bit) & 1) != 0) cnt += 1
      ans = math.max(ans, cnt)
      bit += 1
    }
    ans
  }
}
