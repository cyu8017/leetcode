import scala.collection.mutable.Stack

class MinStack {
  private val stack = Stack[Int]()
  private val minimums = Stack[Int]()
  def push(x: Int): Unit = { stack.push(x); minimums.push(if (minimums.isEmpty) x else math.min(x, minimums.top)) }
  def pop(): Unit = { stack.pop(); minimums.pop() }
  def top(): Int = stack.top
  def getMin(): Int = minimums.top
}