// LeetCode 3752 - Lexicographically Smallest Negated Permutation that Sums to Target
// https://leetcode.com/problems/lexicographically-smallest-negated-permutation-that-sums-to-target/

object Solution {
  def lexicographicallySmallest(n: Int, target: Long): Array[Int] = {
    val total = 1L * n * (n + 1) / 2
    if (target < -total || target > total || (total - target) % 2 != 0) return Array.emptyIntArray
    var remaining = (total - target) / 2
    val negative = new Array[Boolean](n + 1)
    var value = n
    while (value >= 1) {
      if (value <= remaining) {
        negative(value) = true
        remaining -= value
      }
      value -= 1
    }
    val answer = new java.util.ArrayList[Integer]()
    value = n
    while (value >= 1) {
      if (negative(value)) answer.add(-value)
      value -= 1
    }
    value = 1
    while (value <= n) {
      if (!negative(value)) answer.add(value)
      value += 1
    }
    val out = new Array[Int](answer.size())
    var i = 0
    while (i < out.length) {
      out(i) = answer.get(i)
      i += 1
    }
    out
  }
}
