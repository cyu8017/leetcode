// LeetCode 3703 - Remove K-Balanced Substrings
// https://leetcode.com/problems/remove-k-balanced-substrings/

object Solution {
  def removeSubstring(s: String, k: Int): String = {
    val stk = new java.util.ArrayList[Array[Int]]()
    for (c <- s) {
      if (!stk.isEmpty && stk.get(stk.size() - 1)(0) == c.toInt)
        stk.get(stk.size() - 1)(1) += 1
      else stk.add(Array(c.toInt, 1))
      if (c == ')' && stk.size() > 1) {
        val top = stk.get(stk.size() - 1)
        val prev = stk.get(stk.size() - 2)
        if (top(1) == k && prev(1) >= k) {
          stk.remove(stk.size() - 1)
          prev(1) -= k
          if (prev(1) == 0) stk.remove(stk.size() - 1)
        }
      }
    }
    val res = new StringBuilder
    val it = stk.iterator()
    while (it.hasNext) {
      val p = it.next()
      var i = 0
      while (i < p(1)) {
        res.append(p(0).toChar)
        i += 1
      }
    }
    res.toString
  }
}
