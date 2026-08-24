// LeetCode 3953 - Maximum Score with Co-Prime Element
// https://leetcode.com/problems/maximum-score-with-co-prime-element/

import scala.collection.mutable

object Solution {
  def maxScore(nums: Array[Int], maxVal: Int): Int = {
    var limit = maxVal
    val frequency = new Array[Int](100001)
    for (x <- nums) {
      frequency(x) += 1
      if (x > limit) limit = x
    }
    val divisible = new Array[Int](limit + 1)
    var d = 1
    while (d <= limit) {
      var multiple = d
      while (multiple <= limit) {
        if (multiple < frequency.length) divisible(d) += frequency(multiple)
        multiple += d
      }
      d += 1
    }
    var best = -nums.length
    val checked = new Array[Boolean](limit + 1)
    var x = 1
    while (x <= maxVal) {
      best = math.max(best, evaluate(x, x < frequency.length && frequency(x) > 0, checked, divisible))
      x += 1
    }
    for (v <- nums) {
      best = math.max(best, evaluate(v, exists = true, checked, divisible))
    }
    best
  }

  private def evaluate(x: Int, exists: Boolean, checked: Array[Boolean], divisible: Array[Int]): Int = {
    if (checked(x)) return Int.MinValue / 4
    checked(x) = true
    val bad = badCount(x, divisible)
    val cost =
      if (exists) if (x > 1) bad - 1 else 0
      else if (bad > 0) bad else 1
    x - cost
  }

  private def badCount(x: Int, divisible: Array[Int]): Int = {
    val primes = mutable.ArrayBuffer.empty[Int]
    var y = x
    var p = 2
    while (1L * p * p <= y) {
      if (y % p == 0) {
        primes += p
        while (y % p == 0) y /= p
      }
      p += 1
    }
    if (y > 1) primes += y
    var bad = 0
    val psz = primes.size
    var mask = 1
    while (mask < (1 << psz)) {
      var product = 1
      var bits = 0
      var i = 0
      while (i < psz) {
        if (((mask >> i) & 1) != 0) {
          product *= primes(i)
          bits += 1
        }
        i += 1
      }
      if (bits % 2 == 1) bad += divisible(product)
      else bad -= divisible(product)
      mask += 1
    }
    bad
  }
}
