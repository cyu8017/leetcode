// LeetCode 3850 - Count Sequences To K
// https://leetcode.com/problems/count-sequences-to-k/

object Solution {
  private var nums: Array[Int] = _
  private var k: Long = _
  private val f = scala.collection.mutable.Map.empty[String, Int]

  def countSequences(nums: Array[Int], k: Long): Int = {
    this.nums = nums
    this.k = k
    f.clear()
    dfs(0, 1, 1)
  }

  private def gcd(a0: Long, b0: Long): Long = {
    var a = a0
    var b = b0
    while (b != 0) {
      val t = a % b
      a = b
      b = t
    }
    a
  }

  private def dfs(i: Int, p: Long, q: Long): Int = {
    if (i == nums.length) return if (p == k && q == 1) 1 else 0
    val key = i + "," + p + "," + q
    if (f.contains(key)) return f(key)
    var res = dfs(i + 1, p, q)
    val x = nums(i).toLong
    val g1 = gcd(p * x, q)
    res += dfs(i + 1, (p * x) / g1, q / g1)
    val g2 = gcd(p, q * x)
    res += dfs(i + 1, p / g2, (q * x) / g2)
    f(key) = res
    res
  }
}
