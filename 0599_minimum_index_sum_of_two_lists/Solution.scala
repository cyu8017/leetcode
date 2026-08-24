// LeetCode 0599 - Minimum Index Sum of Two Lists
// https://leetcode.com/problems/minimum-index-sum-of-two-lists/

import scala.collection.mutable

object Solution {
  def findRestaurant(list1: Array[String], list2: Array[String]): Array[String] = {
    val index1 = mutable.Map.empty[String, Int]
    var i = 0
    while (i < list1.length) { index1(list1(i)) = i; i += 1 }
    var best = Int.MaxValue
    val answer = mutable.ArrayBuffer.empty[String]
    var j = 0
    while (j < list2.length) {
      index1.get(list2(j)).foreach { i1 =>
        val total = i1 + j
        if (total < best) {
          best = total
          answer.clear()
          answer += list2(j)
        } else if (total == best) {
          answer += list2(j)
        }
      }
      j += 1
    }
    answer.toArray
  }
}
