// LeetCode 0703 - Kth Largest Element in a Stream
// https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest(_k: Int, nums: Array[Int]) {
  private val k = _k
  private val heap = scala.collection.mutable.PriorityQueue.empty[Int](Ordering[Int].reverse)
  for (num <- nums) add(num)

  def add(`val`: Int): Int = {
    heap.enqueue(`val`)
    if (heap.size > k) heap.dequeue()
    heap.head
  }
}
