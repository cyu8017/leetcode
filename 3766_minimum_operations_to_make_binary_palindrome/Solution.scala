// LeetCode 3766 - Minimum Operations To Make Binary Palindrome
// https://leetcode.com/problems/minimum-operations-to-make-binary-palindrome/

object Solution {
  private val PALS: java.util.List[Integer] = {
    val list = new java.util.ArrayList[Integer]()
    val N = 1 << 14
    var i = 0
    while (i < N) {
      val sb = new java.lang.StringBuilder
      var x = i
      if (x == 0) sb.append('0')
      else {
        while (x > 0) {
          sb.append(('0' + (x & 1)).toChar)
          x >>= 1
        }
        sb.reverse()
      }
      if (isPalindrome(sb)) list.add(i)
      i += 1
    }
    list
  }

  private def isPalindrome(s: java.lang.StringBuilder): Boolean = {
    val m = s.length
    var i = 0
    while (i < m / 2) {
      if (s.charAt(i) != s.charAt(m - 1 - i)) return false
      i += 1
    }
    true
  }

  def minOperations(nums: Array[Int]): Array[Int] = {
    val ans = new Array[Int](nums.length)
    var k = 0
    while (k < nums.length) {
      val x = nums(k)
      val it = lowerBound(x)
      var t = Integer.MAX_VALUE
      if (it < PALS.size()) t = PALS.get(it) - x
      if (it > 0) t = math.min(t, x - PALS.get(it - 1))
      ans(k) = t
      k += 1
    }
    ans
  }

  private def lowerBound(x: Int): Int = {
    var lo = 0
    var hi = PALS.size()
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (PALS.get(mid) < x) lo = mid + 1
      else hi = mid
    }
    lo
  }
}
