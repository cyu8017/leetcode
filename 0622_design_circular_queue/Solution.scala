// LeetCode 0622 - Design Circular Queue
// https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue(_k: Int) {
  private val data = Array.fill(_k)(0)
  private val capacity = _k
  private var head = 0
  private var size = 0

  def enQueue(value: Int): Boolean = {
    if (isFull()) return false
    data((head + size) % capacity) = value
    size += 1
    true
  }

  def deQueue(): Boolean = {
    if (isEmpty()) return false
    head = (head + 1) % capacity
    size -= 1
    true
  }

  def Front(): Int = if (isEmpty()) -1 else data(head)

  def Rear(): Int = {
    if (isEmpty()) return -1
    data((head + size - 1) % capacity)
  }

  def isEmpty(): Boolean = size == 0

  def isFull(): Boolean = size == capacity
}
