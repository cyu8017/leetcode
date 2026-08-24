// LeetCode 2326 - Spiral Matrix IV
// https://leetcode.com/problems/spiral-matrix-iv/

class ListNode(var x: Int = 0, var next: ListNode = null)

object Solution {
  def spiralMatrix(m: Int, n: Int, head0: ListNode): Array[Array[Int]] = {
    val ans = Array.fill(m, n)(-1)
    val dirs = Array(Array(0, 1), Array(1, 0), Array(0, -1), Array(-1, 0))
    var r = 0
    var c = 0
    var d = 0
    var head = head0
    while (head != null) {
      ans(r)(c) = head.x
      head = head.next
      var nr = r + dirs(d)(0)
      var nc = c + dirs(d)(1)
      if (nr < 0 || nr >= m || nc < 0 || nc >= n || ans(nr)(nc) != -1) {
        d = (d + 1) % 4
        nr = r + dirs(d)(0)
        nc = c + dirs(d)(1)
      }
      r = nr
      c = nc
    }
    ans
  }
}
