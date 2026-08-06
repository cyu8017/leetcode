// LeetCode 1590 - Make Sum Divisible by P
// https://leetcode.com/problems/make-sum-divisible-by-p/

object Solution {
  def minSubarray(nums: Array[Int], p: Int): Int = {
    val target = nums.map(_.toLong).sum % p
    if (target == 0) return 0
    val seen = scala.collection.mutable.Map(0L -> -1)
    var prefix = 0L
    var answer = nums.length
    for (i <- nums.indices) {
      prefix = (prefix + nums(i)) % p
      val need = (prefix - target + p) % p
      if (seen.contains(need)) answer = math.min(answer, i - seen(need))
      seen(prefix) = i
    }
    if (answer < nums.length) answer else -1
  }
}
