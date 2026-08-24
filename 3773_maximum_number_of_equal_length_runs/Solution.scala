// LeetCode 3773 - Maximum Number Of Equal Length Runs
// https://leetcode.com/problems/maximum-number-of-equal-length-runs/

object Solution {
  def maxSameLengthRuns(s: String): Int = {
    val cnt = new java.util.HashMap[Integer, Integer]()
    val n = s.length
    var ans = 0
    var i = 0
    while (i < n) {
      var j = i + 1
      while (j < n && s.charAt(j) == s.charAt(i)) j += 1
      val m = j - i
      if (!cnt.containsKey(m)) cnt.put(m, 0)
      cnt.merge(m, 1, (a: Integer, b: Integer) => Integer.valueOf(a + b))
      ans = math.max(ans, cnt.get(m))
      i = j
    }
    ans
  }
}
