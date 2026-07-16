// LeetCode 0363 - Max Sum of Rectangle No Larger Than K

// https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/



import scala.collection.mutable



object Solution {

  def maxSumSubmatrix(matrix: Array[Array[Int]], k: Int): Int = {

    val rows = matrix.length

    val cols = if (rows == 0) 0 else matrix(0).length

    var result = Int.MinValue



    for (top <- 0 until rows) {

      val colSums = Array.fill(cols)(0)

      for (bottom <- top until rows) {

        val prefixSums = mutable.ArrayBuffer(0L)

        var running = 0L



        for (col <- 0 until cols) {

          colSums(col) += matrix(bottom)(col)

          running += colSums(col)

          val index = bisectLeft(prefixSums, running - k)

          if (index < prefixSums.length) {

            result = math.max(result, (running - prefixSums(index)).toInt)

          }

          insort(prefixSums, running)

        }

      }

    }



    result

  }



  private def bisectLeft(list: mutable.ArrayBuffer[Long], value: Long): Int = {

    var left = 0

    var right = list.length

    while (left < right) {

      val mid = left + (right - left) / 2

      if (list(mid) < value) left = mid + 1

      else right = mid

    }

    left

  }



  private def insort(list: mutable.ArrayBuffer[Long], value: Long): Unit = {

    list.insert(bisectLeft(list, value), value)

  }

}
