// LeetCode 2183 - Count Array Pairs Divisible by K
// https://leetcode.com/problems/count-array-pairs-divisible-by-k/

object Solution {
  private def gcd(a0: Int, b0: Int): Int = {
    var a = a0
    var b = b0
    while (b != 0) {
      val t = a % b
      a = b
      b = t
    }
    a
  }

  def countPairs(nums: Array[Int], k: Int): Long = {
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    var ans = 0L
    nums.foreach { x =>
      val g1 = gcd(x, k)
      freq.foreach { case (key, v) =>
        if (1L * g1 * key % k == 0) ans += v
      }
      freq(g1) = freq.getOrElse(g1, 0) + 1
    }
    ans
  }
}
