// LeetCode 3309 - Maximum Possible Number by Binary Concatenation
// https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/

object Solution {
  private def toBin(x: Int): String = {
    if (x == 0) return "0"
    val s = new StringBuilder
    var y = x
    while (y > 0) {
      s.insert(0, ('0' + (y & 1)).toChar)
      y >>= 1
    }
    s.toString
  }

  def maxGoodNumber(nums: Array[Int]): Int = {
    val bs = Array.tabulate(3)(i => toBin(nums(i)))
    val idx = Array(0, 1, 2)
    val ans = Array(0)
    perm(0, idx, bs, ans)
    ans(0)
  }

  private def perm(i: Int, idx: Array[Int], bs: Array[String], ans: Array[Int]): Unit = {
    if (i == 3) {
      val s = bs(idx(0)) + bs(idx(1)) + bs(idx(2))
      var v = 0
      for (c <- s) v = v * 2 + (c - '0')
      if (v > ans(0)) ans(0) = v
      return
    }
    var j = i
    while (j < 3) {
      val t = idx(i); idx(i) = idx(j); idx(j) = t
      perm(i + 1, idx, bs, ans)
      val t2 = idx(i); idx(i) = idx(j); idx(j) = t2
      j += 1
    }
  }
}
