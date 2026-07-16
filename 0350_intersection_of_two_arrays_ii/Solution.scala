// LeetCode 0350 - Intersection of Two Arrays II

// https://leetcode.com/problems/intersection-of-two-arrays-ii/



import scala.collection.mutable



object Solution {

  def intersect(nums1: Array[Int], nums2: Array[Int]): Array[Int] = {

    val counts = mutable.Map.empty[Int, Int]

    for (num <- nums1) {

      counts(num) = counts.getOrElse(num, 0) + 1

    }



    val result = mutable.ArrayBuffer.empty[Int]

    for (num <- nums2) {

      val count = counts.getOrElse(num, 0)

      if (count > 0) {

        result += num

        counts(num) = count - 1

      }

    }



    result.toArray

  }

}
