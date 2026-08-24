// LeetCode 2281 - Sum of Total Strength of Wizards
// https://leetcode.com/problems/sum-of-total-strength-of-wizards/

object Solution {
  def totalStrength(strength: Array[Int]): Int = {
    val mod = 1000000007
    val n = strength.length
    val left = new Array[Int](n)
    val right = new Array[Int](n)
    val stack = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < n) {
      while (stack.nonEmpty && strength(stack.last) >= strength(i)) stack.remove(stack.length - 1)
      left(i) = if (stack.isEmpty) -1 else stack.last
      stack += i
      i += 1
    }
    stack.clear()
    i = n - 1
    while (i >= 0) {
      while (stack.nonEmpty && strength(stack.last) > strength(i)) stack.remove(stack.length - 1)
      right(i) = if (stack.isEmpty) n else stack.last
      stack += i
      i -= 1
    }
    val pref = new Array[Long](n + 1)
    val prefPref = new Array[Long](n + 2)
    i = 0
    while (i < n) {
      pref(i + 1) = (pref(i) + strength(i)) % mod
      i += 1
    }
    i = 0
    while (i <= n) {
      prefPref(i + 1) = (prefPref(i) + pref(i)) % mod
      i += 1
    }
    var ans = 0L
    i = 0
    while (i < n) {
      val l = left(i) + 1
      val r = right(i) - 1
      val leftSum = (prefPref(i + 1) - prefPref(l) + mod) % mod
      val rightSum = (prefPref(r + 2) - prefPref(i + 1) + mod) % mod
      val leftCnt = i - l + 1L
      val rightCnt = r - i + 1L
      val contrib = (rightCnt * leftSum % mod - leftCnt * rightSum % mod + mod) % mod
      ans = (ans + contrib * strength(i) % mod) % mod
      i += 1
    }
    ans.toInt
  }
}
