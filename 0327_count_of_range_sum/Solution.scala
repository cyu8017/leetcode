// LeetCode 0327 - Count of Range Sum

// https://leetcode.com/problems/count-of-range-sum/



object Solution {

  private var prefix: Array[Long] = _

  private var temp: Array[Long] = _



  def countRangeSum(nums: Array[Int], lower: Int, upper: Int): Int = {

    prefix = new Array[Long](nums.length + 1)

    temp = new Array[Long](prefix.length)

    for (index <- nums.indices) {

      prefix(index + 1) = prefix(index) + nums(index)

    }

    mergeSort(0, prefix.length - 1, lower.toLong, upper.toLong)

  }



  private def mergeSort(left: Int, right: Int, lower: Long, upper: Long): Int = {

    if (left >= right) {

      return 0

    }

    val mid = (left + right) / 2

    var count = mergeSort(left, mid, lower, upper) + mergeSort(mid + 1, right, lower, upper)

    var start = mid + 1

    var end = mid + 1

    for (index <- left to mid) {

      while (start <= right && prefix(start) - prefix(index) < lower) {

        start += 1

      }

      while (end <= right && prefix(end) - prefix(index) <= upper) {

        end += 1

      }

      count += end - start

    }

    var tempLeft = left

    var tempRight = mid + 1

    var write = left

    while (tempLeft <= mid && tempRight <= right) {

      if (prefix(tempLeft) <= prefix(tempRight)) {

        temp(write) = prefix(tempLeft)

        tempLeft += 1

      } else {

        temp(write) = prefix(tempRight)

        tempRight += 1

      }

      write += 1

    }

    while (tempLeft <= mid) {

      temp(write) = prefix(tempLeft)

      tempLeft += 1

      write += 1

    }

    while (tempRight <= right) {

      temp(write) = prefix(tempRight)

      tempRight += 1

      write += 1

    }

    for (index <- left to right) {

      prefix(index) = temp(index)

    }

    count

  }

}

