// LeetCode 2721 - Execute Asynchronous Functions in Parallel
// https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/

object Solution {
  def promiseAll(functions: List[() => Int]): Array[Int] = {
    val out = new Array[Int](functions.length)
    var i = 0
    while (i < functions.length) {
      out(i) = functions(i)()
      i += 1
    }
    out
  }
}
