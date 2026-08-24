// LeetCode 2761 - Prime Pairs With Target Sum
// https://leetcode.com/problems/prime-pairs-with-target-sum/

object Solution {
  def findPrimePairs(n: Int): List[List[Int]] = {
    val isPrime = Array.fill(n + 1)(false)
    var i = 2
    while (i <= n) {
      isPrime(i) = true
      i += 1
    }
    i = 2
    while (i * i <= n) {
      if (isPrime(i)) {
        var j = i * i
        while (j <= n) {
          isPrime(j) = false
          j += i
        }
      }
      i += 1
    }
    val ans = scala.collection.mutable.ArrayBuffer.empty[List[Int]]
    var x = 2
    while (x <= n / 2) {
      val y = n - x
      if (isPrime(x) && isPrime(y)) ans += List(x, y)
      x += 1
    }
    ans.toList
  }
}
