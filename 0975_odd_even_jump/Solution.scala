// LeetCode 0975 - Odd Even Jump
// https://leetcode.com/problems/odd-even-jump/

object Solution {
  def oddEvenJumps(arr: Array[Int]): Int = {
    val n = arr.length
    val nextHigher = Array.ofDim[Int](n)
    val nextLower = Array.ofDim[Int](n)
    var order = arr.indices.sortBy(i => (arr(i), i)).toArray
    val stack = scala.collection.mutable.ArrayBuffer[Int]()
    order.foreach { i =>
      while (stack.nonEmpty && stack.last < i) {
        nextHigher(stack.last) = i
        stack.remove(stack.length - 1)
      }
      stack += i
    }
    stack.clear()
    order = arr.indices.sortBy(i => (-arr(i), i)).toArray
    order.foreach { i =>
      while (stack.nonEmpty && stack.last < i) {
        nextLower(stack.last) = i
        stack.remove(stack.length - 1)
      }
      stack += i
    }
    val odd = Array.ofDim[Boolean](n)
    val even = Array.ofDim[Boolean](n)
    odd(n - 1) = true
    even(n - 1) = true
    var i = n - 2
    while (i >= 0) {
      if (nextHigher(i) != 0) odd(i) = even(nextHigher(i))
      if (nextLower(i) != 0) even(i) = odd(nextLower(i))
      i -= 1
    }
    odd.count(identity)
  }
}
