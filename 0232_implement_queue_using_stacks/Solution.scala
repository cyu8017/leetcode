// LeetCode 0232 - Implement Queue using Stacks
// https://leetcode.com/problems/implement-queue-using-stacks/

import scala.collection.mutable

class MyQueue {
  private val inputStack = mutable.ArrayStack[Int]()
  private val outputStack = mutable.ArrayStack[Int]()

  private def move(): Unit = {
    if (outputStack.isEmpty) {
      while (inputStack.nonEmpty) {
        outputStack.push(inputStack.pop())
      }
    }
  }

  def push(x: Int): Unit = {
    inputStack.push(x)
  }

  def pop(): Int = {
    move()
    outputStack.pop()
  }

  def peek(): Int = {
    move()
    outputStack.top
  }

  def empty(): Boolean = {
    inputStack.isEmpty && outputStack.isEmpty
  }
}
