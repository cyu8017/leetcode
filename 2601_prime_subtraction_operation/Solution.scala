// LeetCode 2601 - Prime Subtraction Operation
// https://leetcode.com/problems/prime-subtraction-operation/

object Solution {
  def primeSubOperation(nums: Array[Int]): Boolean = {
    var maxV = 0
    nums.foreach(x => if (x > maxV) maxV = x)
    val isP = Array.fill(maxV + 1)(true)
    if (maxV >= 0) isP(0) = false
    if (maxV >= 1) isP(1) = false
    var i = 2
    while (i.toLong * i <= maxV) {
      if (isP(i)) {
        var j = i * i
        while (j <= maxV) {
          isP(j) = false
          j += i
        }
      }
      i += 1
    }
    val primes = scala.collection.mutable.ArrayBuffer.empty[Int]
    i = 2
    while (i <= maxV) {
      if (isP(i)) primes += i
      i += 1
    }
    var prev = 0
    nums.foreach { x =>
      val need = x - prev
      var best = -1
      var pi = 0
      while (pi < primes.length && primes(pi) < need) {
        best = primes(pi)
        pi += 1
      }
      val cur = if (best < 0) x else x - best
      if (cur <= prev) return false
      prev = cur
    }
    true
  }
}
