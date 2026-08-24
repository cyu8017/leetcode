// LeetCode 2636 - Promise Pool
// https://leetcode.com/problems/promise-pool/

object Solution {
  def promisePool(functions: List[() => Int], n: Int): Array[Int] = {
    val ans = new Array[Int](functions.length)
    var i = 0
    while (i < functions.length) {
      ans(i) = functions(i)()
      i += 1
    }
    ans
  }
}
