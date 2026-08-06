// LeetCode 1101 - The Earliest Moment When Everyone Become Friends
// https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

object Solution {
  def earliestAcq(logs: Array[Array[Int]], n: Int): Int = {
    val parent = Array.tabulate(n)(identity)
    def find(x: Int): Int = {
      var cur = x
      while (parent(cur) != cur) {
        parent(cur) = parent(parent(cur))
        cur = parent(cur)
      }
      cur
    }
    def union(a: Int, b: Int): Boolean = {
      val ra = find(a)
      val rb = find(b)
      if (ra == rb) false
      else {
        parent(rb) = ra
        true
      }
    }
    val sorted = logs.sortBy(_(0))
    var components = n
    for (log <- sorted) {
      if (union(log(1), log(2))) {
        components -= 1
        if (components == 1) return log(0)
      }
    }
    -1
  }
}
