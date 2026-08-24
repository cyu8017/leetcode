// LeetCode 2151 - Maximum Good People Based on Statements
// https://leetcode.com/problems/maximum-good-people-based-on-statements/

object Solution {
  private def ok(statements: Array[Array[Int]], n: Int, mask: Int): Boolean = {
    var i = 0
    while (i < n) {
      if ((mask & (1 << i)) != 0) {
        var j = 0
        while (j < n) {
          val s = statements(i)(j)
          if (s != 2) {
            val goodJ = (mask & (1 << j)) != 0
            if ((s == 1 && !goodJ) || (s == 0 && goodJ)) return false
          }
          j += 1
        }
      }
      i += 1
    }
    true
  }

  def maximumGood(statements: Array[Array[Int]]): Int = {
    val n = statements.length
    var ans = 0
    var mask = 0
    while (mask < (1 << n)) {
      if (ok(statements, n, mask)) ans = math.max(ans, Integer.bitCount(mask))
      mask += 1
    }
    ans
  }
}
