// LeetCode 1865 - Finding Pairs With a Certain Sum
// https://leetcode.com/problems/finding-pairs-with-a-certain-sum/

import scala.collection.mutable

class FindSumPairs(_nums1: Array[Int], _nums2: Array[Int]) {
  private val nums1 = _nums1
  private val nums2 = _nums2.clone()
  private val counts = mutable.Map.empty[Int, Int]
  for (num <- nums2) {
    counts(num) = counts.getOrElse(num, 0) + 1
  }

  def add(index: Int, `val`: Int): Unit = {
    counts(nums2(index)) = counts(nums2(index)) - 1
    nums2(index) += `val`
    counts(nums2(index)) = counts.getOrElse(nums2(index), 0) + 1
  }

  def count(tot: Int): Int = {
    var answer = 0
    for (num <- nums1) {
      answer += counts.getOrElse(tot - num, 0)
    }
    answer
  }
}
