// LeetCode 2614 - Prime In Diagonal
// https://leetcode.com/problems/prime-in-diagonal/

object Solution {
  def diagonalPrime(nums: Array[Array[Int]]): Int = {
    val n = nums.length
    var best = 0
    var i = 0
    while (i < n) {
      val a = nums(i)(i)
      val b = nums(i)(n - 1 - i)
      if (isPrime(a) && a > best) best = a
      if (isPrime(b) && b > best) best = b
      i += 1
    }
    best
  }

  private def isPrime(x: Int): Boolean = {
    if (x < 2) return false
    var i = 2
    while (i.toLong * i <= x) {
      if (x % i == 0) return false
      i += 1
    }
    true
  }
}
