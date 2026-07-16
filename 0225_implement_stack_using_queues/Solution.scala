// LeetCode 0225 - Implement Stack using Queues
// https://leetcode.com/problems/implement-stack-using-queues/

import scala.collection.mutable

class MyStack {
  private val queue = mutable.Queue[Int]()

  def push(x: Int): Unit = {
    queue.enqueue(x)
    for (_ <- 0 until queue.size - 1) {
      queue.enqueue(queue.dequeue())
    }
  }

  def pop(): Int = queue.dequeue()

  def top(): Int = queue.head

  def empty(): Boolean = queue.isEmpty
}
