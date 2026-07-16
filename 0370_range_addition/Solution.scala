// LeetCode 0370 - Range Addition

// https://leetcode.com/problems/range-addition/



object Solution {

  def getModifiedArray(length: Int, updates: Array[Array[Int]]): Array[Int] = {

    val diff = Array.fill(length + 1)(0)



    for (update <- updates) {

      val start = update(0)

      val end = update(1)

      val inc = update(2)

      diff(start) += inc

      if (end + 1 < diff.length) {

        diff(end + 1) -= inc

      }

    }



    val result = Array.fill(length)(0)

    var running = 0

    for (index <- 0 until length) {

      running += diff(index)

      result(index) = running

    }

    result

  }

}
