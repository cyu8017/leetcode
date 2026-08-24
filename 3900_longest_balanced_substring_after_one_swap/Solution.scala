// LeetCode 3900 - Longest Balanced Substring After One Swap
// https://leetcode.com/problems/longest-balanced-substring-after-one-swap/

object Solution {
  def longestBalanced(s: String): Int = {
    var cnt0 = 0
    s.foreach { c => if (c == '0') cnt0 += 1 }
    val cnt1 = s.length - cnt0
    val pos = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]
    pos(0) = scala.collection.mutable.ArrayBuffer(-1)
    var ans = 0
    var pre = 0
    var i = 0
    while (i < s.length) {
      if (s.charAt(i) == '1') pre += 1
      else pre -= 1
      pos.getOrElseUpdate(pre, scala.collection.mutable.ArrayBuffer.empty[Int]) += i
      ans = math.max(ans, i - pos(pre)(0))
      if (pos.contains(pre - 2)) {
        val p = pos(pre - 2)
        if ((i - p(0) - 2) / 2 < cnt0) ans = math.max(ans, i - p(0))
        else if (p.length > 1) ans = math.max(ans, i - p(1))
      }
      if (pos.contains(pre + 2)) {
        val p = pos(pre + 2)
        if ((i - p(0) - 2) / 2 < cnt1) ans = math.max(ans, i - p(0))
        else if (p.length > 1) ans = math.max(ans, i - p(1))
      }
      i += 1
    }
    ans
  }
}
