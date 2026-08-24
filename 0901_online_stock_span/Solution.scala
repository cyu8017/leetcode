// LeetCode 0901 - Online Stock Span
// https://leetcode.com/problems/online-stock-span/

class StockSpanner() {
  private val stack = scala.collection.mutable.ArrayBuffer[Array[Int]]()

  def next(price: Int): Int = {
    var span = 1
    while (stack.nonEmpty && stack.last(0) <= price) {
      span += stack.last(1)
      stack.remove(stack.length - 1)
    }
    stack += Array(price, span)
    span
  }
}
