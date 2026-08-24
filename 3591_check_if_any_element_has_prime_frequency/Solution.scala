// LeetCode 3591 - Check if Any Element Has Prime Frequency
// https://leetcode.com/problems/check-if-any-element-has-prime-frequency/

object Solution {
  def isPrime(x: Int): Boolean = {
    if (x < 2) return false
    var i = 2
    while (i * i <= x) {
      if (x % i == 0) return false
      i += 1
    }
    true
  }

  def checkPrimeFrequency(nums: Array[Int]): Boolean = {
    val cnt = scala.collection.mutable.HashMap.empty[Int, Int]
    for (x <- nums) cnt(x) = cnt.getOrElse(x, 0) + 1
    for ((_, v) <- cnt) if (isPrime(v)) return true
    false
  }
}
