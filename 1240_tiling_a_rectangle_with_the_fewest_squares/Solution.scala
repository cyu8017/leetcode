// LeetCode 1240 - Tiling a Rectangle with the Fewest Squares
// https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

object Solution {
  def tilingRectangle(n: Int, m: Int): Int = {
    var nn = n
    var mm = m
    if (nn > mm) { val t = nn; nn = mm; mm = t }
    val heights = Array.fill(mm)(0)
    var best = nn * mm
    def search(used: Int): Unit = {
      if (used >= best) return
      val low = heights.min
      if (low == nn) {
        best = used
        return
      }
      val left = heights.indexOf(low)
      var right = left
      while (right < mm && heights(right) == low) right += 1
      val maxSize = math.min(nn - low, right - left)
      for (size <- maxSize to 1 by -1) {
        for (i <- left until left + size) heights(i) = low + size
        search(used + 1)
        for (i <- left until left + size) heights(i) = low
      }
    }
    search(0)
    best
  }
}
