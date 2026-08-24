// LeetCode 3714 - Longest Balanced Substring II
// https://leetcode.com/problems/longest-balanced-substring-ii/

object Solution {
  private def calc1(s: String): Int = {
    var res = 0
    val n = s.length
    var i = 0
    while (i < n) {
      var j = i + 1
      while (j < n && s.charAt(j) == s.charAt(i)) j += 1
      res = math.max(res, j - i)
      i = j
    }
    res
  }

  private def calc2(s: String, a: Char, b: Char): Int = {
    var res = 0
    val n = s.length
    var i = 0
    while (i < n) {
      while (i < n && s.charAt(i) != a && s.charAt(i) != b) i += 1
      val pos = new java.util.HashMap[Integer, Integer]()
      pos.put(0, i - 1)
      var d = 0
      while (i < n && (s.charAt(i) == a || s.charAt(i) == b)) {
        if (s.charAt(i) == a) d += 1
        else d -= 1
        if (pos.containsKey(d)) res = math.max(res, i - pos.get(d))
        else pos.put(d, i)
        i += 1
      }
    }
    res
  }

  private def calc3(s: String): Int = {
    val pos = new java.util.HashMap[java.lang.Long, Integer]()
    pos.put(0L, -1)
    val cnt = new Array[Int](3)
    var res = 0
    var i = 0
    while (i < s.length) {
      cnt(s.charAt(i) - 'a') += 1
      val x = cnt(0) - cnt(1)
      val y = cnt(1) - cnt(2)
      val k = (x.toLong << 32) ^ (y & 0xffffffffL)
      if (pos.containsKey(k)) res = math.max(res, i - pos.get(k))
      else pos.put(k, i)
      i += 1
    }
    res
  }

  def longestBalanced(s: String): Int = {
    val x = calc1(s)
    val y = math.max(calc2(s, 'a', 'b'), math.max(calc2(s, 'b', 'c'), calc2(s, 'a', 'c')))
    val z = calc3(s)
    math.max(x, math.max(y, z))
  }
}
