// LeetCode 2361 - Minimum Costs Using the Train Line
// https://leetcode.com/problems/minimum-costs-using-the-train-line/

object Solution {
  def minimumCosts(regular: Array[Int], express: Array[Int], expressCost: Int): Array[Long] = {
    val n = regular.length
    val ans = Array.fill(n)(0L)
    var reg = 0L
    var exp = expressCost.toLong
    var i = 0
    while (i < n) {
      val nextReg = math.min(reg + regular(i), exp + express(i))
      val nextExp = math.min(reg + regular(i) + expressCost, exp + express(i))
      reg = nextReg
      exp = nextExp
      ans(i) = math.min(reg, exp)
      i += 1
    }
    ans
  }
}
