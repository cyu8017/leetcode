// LeetCode 3697 - Compute Decimal Representation
// https://leetcode.com/problems/compute-decimal-representation/

object Solution {
  def decimalRepresentation(n0: Int): Array[Int] = {
    val ans = new java.util.ArrayList[Integer]()
    var p = 1
    var n = n0
    while (n > 0) {
      val v = n % 10
      n /= 10
      if (v != 0) ans.add(p * v)
      p *= 10
    }
    java.util.Collections.reverse(ans)
    val res = new Array[Int](ans.size())
    var i = 0
    while (i < ans.size()) {
      res(i) = ans.get(i)
      i += 1
    }
    res
  }
}
