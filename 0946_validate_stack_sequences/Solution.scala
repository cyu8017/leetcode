// LeetCode 0946 - Validate Stack Sequences
// https://leetcode.com/problems/validate-stack-sequences/

object Solution {
  def validateStackSequences(pushed: Array[Int], popped: Array[Int]): Boolean = {
    val stack = scala.collection.mutable.ArrayBuffer[Int]()
    var j = 0
    pushed.foreach { x =>
      stack += x
      while (stack.nonEmpty && stack.last == popped(j)) {
        stack.remove(stack.length - 1)
        j += 1
      }
    }
    stack.isEmpty
  }
}
