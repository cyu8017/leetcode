// LeetCode 0315 - Count of Smaller Numbers After Self

// https://leetcode.com/problems/count-of-smaller-numbers-after-self/



import scala.collection.mutable



object Solution {

  def countSmaller(nums: Array[Int]): List[Int] = {

    val sortedNums = mutable.ListBuffer.empty[Int]

    val result = mutable.ListBuffer.empty[Int]

    for (index <- nums.indices.reverse) {

      val num = nums(index)

      val position = lowerBound(sortedNums, num)

      result += position

      sortedNums.insert(position, num)

    }

    result.reverse.toList

  }



  private def lowerBound(list: mutable.ListBuffer[Int], target: Int): Int = {

    var left = 0

    var right = list.length

    while (left < right) {

      val mid = left + (right - left) / 2

      if (list(mid) < target) {

        left = mid + 1

      } else {

        right = mid

      }

    }

    left

  }

}

