// LeetCode 2209 - Minimum White Tiles After Covering With Carpets
// https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/

object Solution {
  def minimumWhiteTiles(floor: String, numCarpets: Int, carpetLen: Int): Int = {
    val n = floor.length
    val dp = Array.fill(numCarpets + 1, n + 1)(1 << 30)
    dp(0)(0) = 0
    var j = 1
    while (j <= n) {
      dp(0)(j) = dp(0)(j - 1) + (if (floor.charAt(j - 1) == '1') 1 else 0)
      j += 1
    }
    var c = 1
    while (c <= numCarpets) {
      dp(c)(0) = 0
      j = 1
      while (j <= n) {
        dp(c)(j) = dp(c)(j - 1) + (if (floor.charAt(j - 1) == '1') 1 else 0)
        val start = math.max(0, j - carpetLen)
        dp(c)(j) = math.min(dp(c)(j), dp(c - 1)(start))
        j += 1
      }
      c += 1
    }
    dp(numCarpets)(n)
  }
}
