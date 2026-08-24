// LeetCode 2690 - Infinite Method Object
// https://leetcode.com/problems/infinite-method-object/

object Solution {
  def createInfiniteObject(): String => String = {
    (_: String) => "Hello World"
  }
}
