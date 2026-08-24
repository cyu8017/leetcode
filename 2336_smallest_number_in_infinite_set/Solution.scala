// LeetCode 2336 - Smallest Number in Infinite Set
// https://leetcode.com/problems/smallest-number-in-infinite-set/

class SmallestInfiniteSet() {
  private var next = 1
  private val added = scala.collection.mutable.HashSet.empty[Int]
  private val heap = scala.collection.mutable.PriorityQueue.empty[Int](Ordering[Int].reverse)

  def popSmallest(): Int = {
    if (heap.nonEmpty) {
      val x = heap.dequeue()
      added.remove(x)
      return x
    }
    val x = next
    next += 1
    x
  }

  def addBack(num: Int): Unit = {
    if (num < next && added.add(num)) heap.enqueue(num)
  }
}
