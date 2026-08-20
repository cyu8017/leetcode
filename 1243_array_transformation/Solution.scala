// LeetCode 1243 - Array Transformation
// https://leetcode.com/problems/array-transformation/

object Solution {
  def transformArray(arr: Array[Int]): List[Int] = {
    var cur = arr.clone()
    var changed = true
    while (changed) {
      changed = false
      val nxt = cur.clone()
      for (i <- 1 until cur.length - 1) {
        if (cur(i) < cur(i - 1) && cur(i) < cur(i + 1)) {
          nxt(i) += 1
          changed = true
        } else if (cur(i) > cur(i - 1) && cur(i) > cur(i + 1)) {
          nxt(i) -= 1
          changed = true
        }
      }
      cur = nxt
    }
    cur.toList
  }
}
