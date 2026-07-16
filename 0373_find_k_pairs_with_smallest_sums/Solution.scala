// LeetCode 0373 - Find K Pairs with Smallest Sums

// https://leetcode.com/problems/find-k-pairs-with-smallest-sums/



import scala.collection.mutable



object Solution {

  def kSmallestPairs(nums1: Array[Int], nums2: Array[Int], k: Int): List[List[Int]] = {

    if (nums1.isEmpty || nums2.isEmpty || k == 0) {

      return List.empty

    }



    val heap = mutable.PriorityQueue.empty[(Int, Int, Int)](Ordering.by(-_._1))

    val result = mutable.ArrayBuffer.empty[List[Int]]



    for (index <- 0 until math.min(nums1.length, k)) {

      heap.enqueue((nums1(index) + nums2(0), index, 0))

    }



    while (heap.nonEmpty && result.length < k) {

      val (_, index1, index2) = heap.dequeue()

      result += List(nums1(index1), nums2(index2))

      if (index2 + 1 < nums2.length) {

        heap.enqueue((nums1(index1) + nums2(index2 + 1), index1, index2 + 1))

      }

    }



    result.toList

  }

}
