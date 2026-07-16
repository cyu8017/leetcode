// LeetCode 0484 - Find Permutation
// https://leetcode.com/problems/find-permutation/

import scala.collection.mutable

object Solution {
  def findPermutation(s: String): Array[Int] = {
    val stack = mutable.ArrayBuffer(1)
    val result = mutable.ArrayBuffer.empty[Int]
    s.foreach { ch =>
      if (ch == 'I') {
        while (stack.nonEmpty) {
          result += stack.remove(stack.length - 1)
        }
      }
      stack += stack.length + result.length + 1
    }
    while (stack.nonEmpty) {
      result += stack.remove(stack.length - 1)
    }
    result.toArray
  }
}
