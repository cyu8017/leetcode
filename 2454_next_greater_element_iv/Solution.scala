// LeetCode 2454 - Next Greater Element IV
// https://leetcode.com/problems/next-greater-element-iv/

object Solution {
  def secondGreaterElement(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val ans = Array.fill(n)(-1)
    val stack1 = scala.collection.mutable.ArrayBuffer.empty[Int]
    val stack2 = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < n) {
      val x = nums(i)
      while (stack2.nonEmpty && nums(stack2.last) < x) {
        ans(stack2.last) = x
        stack2.remove(stack2.length - 1)
      }
      val tmp = scala.collection.mutable.ArrayBuffer.empty[Int]
      while (stack1.nonEmpty && nums(stack1.last) < x) {
        tmp += stack1.last
        stack1.remove(stack1.length - 1)
      }
      var j = tmp.length - 1
      while (j >= 0) {
        stack2 += tmp(j)
        j -= 1
      }
      stack1 += i
      i += 1
    }
    ans
  }
}
