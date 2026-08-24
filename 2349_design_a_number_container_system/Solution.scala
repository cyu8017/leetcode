// LeetCode 2349 - Design a Number Container System
// https://leetcode.com/problems/design-a-number-container-system/

class NumberContainers() {
  private val idx = scala.collection.mutable.Map.empty[Int, Int]
  private val heap = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.TreeSet[Int]]

  def change(index: Int, number: Int): Unit = {
    idx(index) = number
    heap.getOrElseUpdate(number, scala.collection.mutable.TreeSet.empty[Int]) += index
  }

  def find(number: Int): Int = {
    val h = heap.getOrElse(number, return -1)
    while (h.nonEmpty) {
      val i = h.head
      if (idx.get(i).contains(number)) return i
      h -= i
    }
    -1
  }
}
