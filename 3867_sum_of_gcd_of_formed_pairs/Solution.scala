// LeetCode 3867 - Sum Of Gcd Of Formed Pairs
// https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/

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

  def gcdSum(nums: Array[Int]): Long = {
    val n = nums.length
    val prefixGcd = new Array[Int](n)
    var mx = 0
    var i = 0
    while (i < n) {
      mx = math.max(mx, nums(i))
      prefixGcd(i) = gcd(nums(i), mx)
      i += 1
    }
    java.util.Arrays.sort(prefixGcd)
    var ans = 0L
    i = 0
    while (i < n / 2) {
      ans += gcd(prefixGcd(i), prefixGcd(n - i - 1))
      i += 1
    }
    ans
  }
}
