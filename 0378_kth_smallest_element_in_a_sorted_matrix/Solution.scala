// LeetCode 0378 - Kth Smallest Element in a Sorted Matrix

// https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/



object Solution {

  def kthSmallest(matrix: Array[Array[Int]], k: Int): Int = {

    val rows = matrix.length

    var left = matrix(0)(0)

    var right = matrix(rows - 1)(rows - 1)



    while (left < right) {

      val mid = left + (right - left) / 2

      var count = 0

      var column = rows - 1



      for (row <- 0 until rows) {

        while (column >= 0 && matrix(row)(column) > mid) {

          column -= 1

        }

        count += column + 1

      }



      if (count < k) {

        left = mid + 1

      } else {

        right = mid

      }

    }



    left

  }

}
