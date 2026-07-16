class Solution {
  def calculateMinimumHP(dungeon: Array[Array[Int]]): Int = {
    val rows = dungeon.length
    val cols = dungeon(0).length
    val dp = Array.fill(rows + 1, cols + 1)(Int.MaxValue)
    dp(rows)(cols - 1) = 1
    dp(rows - 1)(cols) = 1

    for (r <- rows - 1 to 0 by -1; c <- cols - 1 to 0 by -1) {
      val needed = math.min(dp(r + 1)(c), dp(r)(c + 1)) - dungeon(r)(c)
      dp(r)(c) = math.max(1, needed)
    }
    dp(0)(0)
  }
}
