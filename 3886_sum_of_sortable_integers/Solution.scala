// LeetCode 3886 - Sum of Sortable Integers
// https://leetcode.com/problems/sum-of-sortable-integers/

object Solution {
  private def rotationMatches(block: Array[Int], target: Array[Int]): Boolean = {
    val k = block.length
    val prefix = new Array[Int](k)
    var i = 1
    while (i < k) {
      var j = prefix(i - 1)
      while (j > 0 && target(i) != target(j)) j = prefix(j - 1)
      if (target(i) == target(j)) j += 1
      prefix(i) = j
      i += 1
    }
    var matched = 0
    i = 0
    while (i < 2 * k - 1) {
      val x = block(i % k)
      while (matched > 0 && x != target(matched)) matched = prefix(matched - 1)
      if (x == target(matched)) matched += 1
      if (matched == k) return true
      i += 1
    }
    false
  }

  def sumOfSortableIntegers(nums: Array[Int]): Int = {
    val n = nums.length
    val sorted = nums.clone()
    java.util.Arrays.sort(sorted)
    val divisors = scala.collection.mutable.ArrayBuffer.empty[Int]
    var d = 1
    while (d * d <= n) {
      if (n % d == 0) {
        divisors += d
        if (d * d != n) divisors += n / d
      }
      d += 1
    }
    var answer = 0
    divisors.foreach { k =>
      var ok = true
      var start = 0
      while (start < n && ok) {
        val block = java.util.Arrays.copyOfRange(nums, start, start + k)
        val target = java.util.Arrays.copyOfRange(sorted, start, start + k)
        if (!rotationMatches(block, target)) ok = false
        start += k
      }
      if (ok) answer += k
    }
    answer
  }
}
