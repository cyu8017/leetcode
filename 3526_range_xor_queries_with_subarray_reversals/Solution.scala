// LeetCode 3526 - Range XOR Queries with Subarray Reversals
// https://leetcode.com/problems/range-xor-queries-with-subarray-reversals/

object Solution {
  def getResults(nums: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    val a = nums.clone()
    val ans = new java.util.ArrayList[Integer]()
    for (q <- queries) {
      val typ = q(0)
      if (typ == 1) {
        var l = q(1)
        var r = q(2)
        while (l < r) {
          val tmp = a(l); a(l) = a(r); a(r) = tmp
          l += 1; r -= 1
        }
      } else if (typ == 2) {
        val l = q(1); val r = q(2)
        var x = 0
        var i = l
        while (i <= r) { x ^= a(i); i += 1 }
        ans.add(x)
      } else {
        a(q(1)) = q(2)
      }
    }
    val out = new Array[Int](ans.size())
    var t = 0
    while (t < ans.size()) { out(t) = ans.get(t); t += 1 }
    out
  }
}
