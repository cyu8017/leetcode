// LeetCode 2967 - Minimum Cost to Make Array Equalindromic
// https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/

object Solution {
  private def makePal(x: Int): Int = {
    val ch = x.toString.toCharArray
    var i = 0
    var j = ch.length - 1
    while (i < j) { ch(j) = ch(i); i += 1; j -= 1 }
    new String(ch).toInt
  }

  private def cost(nums: Array[Int], p: Int): Long = {
    var c = 0L
    for (v <- nums) c += math.abs(v.toLong - p)
    c
  }

  def minimumCost(nums: Array[Int]): Long = {
    scala.util.Sorting.quickSort(nums)
    val n = nums.length
    val median = nums(n / 2)
    val candidates = scala.collection.mutable.ArrayBuffer[Int](makePal(median))
    val s = median.toString
    val half = s.substring(0, (s.length + 1) / 2).toInt
    var d = -2
    while (d <= 2) {
      val h = half + d
      if (h > 0) {
        val hs = h.toString
        val pal = if (s.length % 2 == 0) {
          val rb = hs.toCharArray
          var i = 0
          var j = rb.length - 1
          while (i < j) { val tmp = rb(i); rb(i) = rb(j); rb(j) = tmp; i += 1; j -= 1 }
          hs + new String(rb)
        } else {
          val prefix = hs.substring(0, hs.length - 1)
          val rb = prefix.toCharArray
          var i = 0
          var j = rb.length - 1
          while (i < j) { val tmp = rb(i); rb(i) = rb(j); rb(j) = tmp; i += 1; j -= 1 }
          hs + new String(rb)
        }
        try { candidates += pal.toInt } catch { case _: NumberFormatException => () }
      }
      d += 1
    }
    for (v <- Array(1, 9, 11, 99, 101)) candidates += v
    var ans = Long.MaxValue / 4
    for (p <- candidates) if (p > 0) ans = math.min(ans, cost(nums, p))
    ans
  }
}
