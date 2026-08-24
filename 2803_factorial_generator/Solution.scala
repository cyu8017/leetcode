// LeetCode 2803 - Factorial Generator
// https://leetcode.com/problems/factorial-generator/

object Solution {
  def factorialGenerator(n: Int): List[Int] = {
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    var cur = 1
    var i = 1
    while (i <= n) {
      cur *= i
      ans += cur
      i += 1
    }
    ans.toList
  }
}
