// LeetCode 0321 - Create Maximum Number

// https://leetcode.com/problems/create-maximum-number/



import scala.collection.mutable



object Solution {

  def maxNumber(nums1: Array[Int], nums2: Array[Int], k: Int): Array[Int] = {

    var best = Array.empty[Int]

    val minFirst = math.max(0, k - nums2.length)

    val maxFirst = math.min(k, nums1.length)

    for (takeFirst <- minFirst to maxFirst) {

      val takeSecond = k - takeFirst

      val candidate = merge(pickMax(nums1, takeFirst), pickMax(nums2, takeSecond))

      if (compare(candidate, best) > 0) {

        best = candidate

      }

    }

    best

  }



  private def pickMax(values: Array[Int], count: Int): Array[Int] = {

    var drop = values.length - count

    val stack = mutable.ListBuffer.empty[Int]

    for (value <- values) {

      while (drop > 0 && stack.nonEmpty && stack.last < value) {

        stack.remove(stack.length - 1)

        drop -= 1

      }

      stack += value

    }

    stack.take(count).toArray

  }



  private def merge(first: Array[Int], second: Array[Int]): Array[Int] = {

    val result = new Array[Int](first.length + second.length)

    var left = 0

    var right = 0

    var write = 0

    while (left < first.length && right < second.length) {

      if (compareSuffix(first, left, second, right) > 0) {

        result(write) = first(left)

        left += 1

      } else {

        result(write) = second(right)

        right += 1

      }

      write += 1

    }

    while (left < first.length) {

      result(write) = first(left)

      left += 1

      write += 1

    }

    while (right < second.length) {

      result(write) = second(right)

      right += 1

      write += 1

    }

    result

  }



  private def compareSuffix(first: Array[Int], left: Int, second: Array[Int], right: Int): Int = {

    var index = left

    var other = right

    while (index < first.length && other < second.length) {

      if (first(index) != second(other)) {

        return first(index).compare(second(other))

      }

      index += 1

      other += 1

    }

    (first.length - left).compare(second.length - right)

  }



  private def compare(left: Array[Int], right: Array[Int]): Int = {

    if (left.length != right.length) {

      return left.length.compare(right.length)

    }

    for (index <- left.indices) {

      if (left(index) != right(index)) {

        return left(index).compare(right(index))

      }

    }

    0

  }

}

