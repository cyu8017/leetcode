// LeetCode 0360 - Sort Transformed Array

// https://leetcode.com/problems/sort-transformed-array/



object Solution {

  def sortTransformedArray(nums: Array[Int], a: Int, b: Int, c: Int): Array[Int] = {

    var left = 0

    var right = nums.length - 1

    val result = Array.fill(nums.length)(0)

    var index = if (a > 0) nums.length - 1 else 0

    val step = if (a > 0) -1 else 1



    while (left <= right) {

      val leftValue = transform(nums(left), a, b, c)

      val rightValue = transform(nums(right), a, b, c)



      if (a > 0) {

        if (leftValue > rightValue) {

          result(index) = leftValue

          left += 1

        } else {

          result(index) = rightValue

          right -= 1

        }

      } else if (leftValue < rightValue) {

        result(index) = leftValue

        left += 1

      } else {

        result(index) = rightValue

        right -= 1

      }



      index += step

    }



    result

  }



  private def transform(value: Int, a: Int, b: Int, c: Int): Int = {

    a * value * value + b * value + c

  }

}
