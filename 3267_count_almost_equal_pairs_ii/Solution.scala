// LeetCode 3267 - Count Almost Equal Pairs II
// https://leetcode.com/problems/count-almost-equal-pairs-ii/

object Solution {
  def countPairs(nums: Array[Int]): Int = {
    var ans = 0
    var i = 0
    while (i < nums.length) {
      var j = i + 1
      while (j < nums.length) {
        if (almostEqual(nums(i), nums(j))) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }

  def padNum(x0: Int): String = {
    if (x0 == 0) return "0"
    var x = x0
    val b = new StringBuilder
    while (x > 0) {
      b.insert(0, ('0' + x % 10).toChar)
      x /= 10
    }
    b.toString
  }

  def almostEqual(a: Int, b: Int): Boolean = {
    var sa = padNum(a)
    var sb = padNum(b)
    while (sa.length < sb.length) sa = "0" + sa
    while (sb.length < sa.length) sb = "0" + sb
    if (sa == sb) return true
    canWithSwaps(sa, sb, 2)
  }

  def canWithSwaps(sa: String, sb: String, maxSwap: Int): Boolean = {
    val arr = sa.toCharArray
    dfs(arr, sb, 0, maxSwap)
  }

  def dfs(arr: Array[Char], sb: String, start: Int, left: Int): Boolean = {
    if (new String(arr) == sb) return true
    if (left == 0) return false
    var i = start
    while (i < arr.length) {
      if (arr(i) != sb.charAt(i)) {
        var j = i + 1
        while (j < arr.length) {
          if (arr(j) == sb.charAt(i)) {
            val tmp = arr(i); arr(i) = arr(j); arr(j) = tmp
            if (dfs(arr, sb, i + 1, left - 1)) return true
            val tmp2 = arr(i); arr(i) = arr(j); arr(j) = tmp2
          }
          j += 1
        }
        return false
      }
      i += 1
    }
    new String(arr) == sb
  }
}
