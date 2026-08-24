// LeetCode 0641 - Design Circular Deque
// https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque(_k: Int) {
  private val data = Array.fill(_k)(0)
  private val capacity = _k
  private var front = 0
  private var size = 0

  def insertFront(value: Int): Boolean = {
    if (isFull()) return false
    front = (front - 1 + capacity) % capacity
    data(front) = value
    size += 1
    true
  }

  def insertLast(value: Int): Boolean = {
    if (isFull()) return false
    data((front + size) % capacity) = value
    size += 1
    true
  }

  def deleteFront(): Boolean = {
    if (isEmpty()) return false
    front = (front + 1) % capacity
    size -= 1
    true
  }

  def deleteLast(): Boolean = {
    if (isEmpty()) return false
    size -= 1
    true
  }

  def getFront(): Int = if (isEmpty()) -1 else data(front)

  def getRear(): Int = {
    if (isEmpty()) return -1
    data((front + size - 1) % capacity)
  }

  def isEmpty(): Boolean = size == 0

  def isFull(): Boolean = size == capacity
}
