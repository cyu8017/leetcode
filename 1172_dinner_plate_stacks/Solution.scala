// LeetCode 1172 - Dinner Plate Stacks
// https://leetcode.com/problems/dinner-plate-stacks/

class DinnerPlates(_capacity: Int) {
  private val capacity = _capacity
  private val stacks = scala.collection.mutable.ArrayBuffer.empty[scala.collection.mutable.ArrayBuffer[Int]]
  private val available = scala.collection.mutable.PriorityQueue.empty[Int](Ordering[Int].reverse)

  def push(`val`: Int): Unit = {
    while (available.nonEmpty && (available.head >= stacks.length || stacks(available.head).length == capacity)) {
      available.dequeue()
    }
    if (available.isEmpty) {
      stacks += scala.collection.mutable.ArrayBuffer.empty[Int]
      available.enqueue(stacks.length - 1)
    }
    val idx = available.head
    stacks(idx) += `val`
    if (stacks(idx).length == capacity) available.dequeue()
  }

  def pop(): Int = {
    while (stacks.nonEmpty && stacks.last.isEmpty) stacks.remove(stacks.length - 1)
    if (stacks.isEmpty) -1 else popAtStack(stacks.length - 1)
  }

  def popAtStack(index: Int): Int = {
    if (index < 0 || index >= stacks.length || stacks(index).isEmpty) return -1
    if (stacks(index).length == capacity) available.enqueue(index)
    stacks(index).remove(stacks(index).length - 1)
  }
}
