// LeetCode 3858 - Minimum Bitwise Or From Grid
// https://leetcode.com/problems/minimum-bitwise-or-from-grid/

object Solution {
  private def bitLen(x0: Int): Int = {
    var x = x0
    if (x == 0) return 0
    var n = 0
    while (x > 0) { n += 1; x >>= 1 }
    n
  }

  def minimumOR(grid: Array[Array[Int]]): Int = {
    var mx = 0
    grid.foreach { row => row.foreach { x => mx = math.max(mx, x) } }
    val m = bitLen(mx)
    var ans = 0
    var i = m - 1
    while (i >= 0) {
      val mask = ans | ((1 << i) - 1)
      var needBit = false
      grid.foreach { row =>
        if (!needBit) {
          var found = false
          row.foreach { x => if ((x | mask) == mask) found = true }
          if (!found) {
            ans |= 1 << i
            needBit = true
          }
        }
      }
      i -= 1
    }
    ans
  }
}
