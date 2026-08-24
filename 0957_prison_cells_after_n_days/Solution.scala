// LeetCode 0957 - Prison Cells After N Days
// https://leetcode.com/problems/prison-cells-after-n-days/

object Solution {
  def prisonAfterNDays(cells: Array[Int], n: Int): Array[Int] = {
    val seen = scala.collection.mutable.Map.empty[String, Int]
    var state = cells.clone()
    var remain = n
    while (remain > 0) {
      val key = state.mkString(",")
      if (seen.contains(key)) {
        val cycle = seen(key) - remain
        remain %= cycle
        if (remain == 0) return state
      }
      seen(key) = remain
      val nxt = Array.ofDim[Int](8)
      var i = 1
      while (i <= 6) {
        nxt(i) = if (state(i - 1) == state(i + 1)) 1 else 0
        i += 1
      }
      state = nxt
      remain -= 1
    }
    state
  }
}
