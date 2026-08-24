// LeetCode 2170 - Minimum Operations to Make the Array Alternating
// https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/

object Solution {
  private def top2(nums: Array[Int], idxs: Seq[Int]): Array[Int] = {
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    idxs.foreach(i => freq(nums(i)) = freq.getOrElse(nums(i), 0) + 1)
    var a = 0
    var ac = 0
    var b = 0
    var bc = 0
    freq.foreach { case (v, c) =>
      if (c > ac) { b = a; bc = ac; a = v; ac = c }
      else if (c > bc) { b = v; bc = c }
    }
    Array(a, ac, b, bc)
  }

  def minimumOperations(nums: Array[Int]): Int = {
    val n = nums.length
    if (n == 1) return 0
    val even = (0 until n).filter(_ % 2 == 0)
    val odd = (0 until n).filter(_ % 2 != 0)
    val e = top2(nums, even)
    val o = top2(nums, odd)
    if (e(0) != o(0)) n - e(1) - o(1)
    else math.min(n - e(1) - o(3), n - e(3) - o(1))
  }
}
