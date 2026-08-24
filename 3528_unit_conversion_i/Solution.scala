// LeetCode 3528 - Unit Conversion I
// https://leetcode.com/problems/unit-conversion-i/

object Solution {
  def baseUnitConversions(conversions: Array[Array[Int]]): Array[Int] = {
    val mod = 1000000007
    val n = conversions.length + 1
    val g = Array.fill(n)(new java.util.ArrayList[Array[Int]]())
    for (e <- conversions) g(e(0)).add(Array(e(1), e(2)))
    val ans = new Array[Int](n)
    def dfs(s: Int, mul: Int): Unit = {
      ans(s) = mul
      val it = g(s).iterator()
      while (it.hasNext) {
        val e = it.next()
        dfs(e(0), ((1L * mul * e(1)) % mod).toInt)
      }
    }
    dfs(0, 1)
    ans
  }
}
