// LeetCode 0444 - Sequence Reconstruction
// https://leetcode.com/problems/sequence-reconstruction/

import scala.collection.mutable

object Solution {
  def sequenceReconstruction(nums: Array[Int], sequences: Array[Array[Int]]): Boolean = {
    val indegree = mutable.Map.from(nums.map(value => value -> 0))
    val graph = mutable.Map.from(nums.map(value => value -> mutable.Set.empty[Int]))
    val seenEdges = mutable.Set.empty[(Int, Int)]

    for (sequence <- sequences) {
      var index = 0
      while (index < sequence.length - 1) {
        val left = sequence(index)
        val right = sequence(index + 1)
        if (!seenEdges.contains((left, right))) {
          seenEdges.add((left, right))
          graph(left).add(right)
          indegree(right) += 1
        }
        index += 1
      }
    }

    val queue = mutable.Queue.from(nums.filter(value => indegree(value) == 0))
    val order = mutable.ListBuffer.empty[Int]
    while (queue.nonEmpty) {
      if (queue.length > 1) {
        return false
      }
      val node = queue.dequeue()
      order += node
      for (neighbor <- graph(node)) {
        indegree(neighbor) -= 1
        if (indegree(neighbor) == 0) {
          queue.enqueue(neighbor)
        }
      }
    }

    order.toArray.sameElements(nums)
  }
}
