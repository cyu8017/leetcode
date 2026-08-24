// LeetCode 0716 - Max Stack
// https://leetcode.com/problems/max-stack/

class MaxStack() {
  private val stack = scala.collection.mutable.ArrayBuffer.empty[Int]
  private val maxes = scala.collection.mutable.ArrayBuffer.empty[Int]

  def push(x: Int): Unit = {
    stack += x
    maxes += (if (maxes.isEmpty) x else math.max(x, maxes.last))
  }

  def pop(): Int = {
    maxes.remove(maxes.length - 1)
    stack.remove(stack.length - 1)
  }

  def top(): Int = stack.last

  def peekMax(): Int = maxes.last

  def popMax(): Int = {
    val maxVal = peekMax()
    val buffer = scala.collection.mutable.ArrayBuffer.empty[Int]
    while (top() != maxVal) buffer += pop()
    pop()
    var i = buffer.length - 1
    while (i >= 0) {
      push(buffer(i))
      i -= 1
    }
    maxVal
  }
}
