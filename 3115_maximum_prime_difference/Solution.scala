// LeetCode 3115 - Maximum Prime Difference
// https://leetcode.com/problems/maximum-prime-difference/

object Solution {
  def maximumPrimeDifference(nums: Array[Int]): Int = {
    def isPrime(n: Int): Boolean = {
      if (n < 2) return false
      var i = 2
      while (i <= n / i) {
        if (n % i == 0) return false
        i += 1
      }
      true
    }

    var i = 0
    while (true) {
      if (isPrime(nums(i))) {
        var j = nums.length - 1
        while (true) {
          if (isPrime(nums(j))) return j - i
          j -= 1
        }
      }
      i += 1
    }
    0
  }
}
