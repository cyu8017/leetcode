// LeetCode 2197 - Replace Non-Coprime Numbers in Array
// https://leetcode.com/problems/replace-non-coprime-numbers-in-array/

object Solution {
  def replaceNonCoprimes(nums: Array[Int]): Array[Int] = {
    def gcd(a0: Int, b0: Int): Int = {
      var a = a0
      var b = b0
      while (b != 0) {
        val t = a % b
        a = b
        b = t
      }
      a
    }
    val stack = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (x0 <- nums) {
      var x = x0
      var merged = true
      while (merged && stack.nonEmpty) {
        val g = gcd(stack.last, x)
        if (g == 1) merged = false
        else {
          x = stack.last / g * x
          stack.remove(stack.length - 1)
        }
      }
      stack += x
    }
    stack.toArray
  }
}
