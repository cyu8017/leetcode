// LeetCode 0354 - Russian Doll Envelopes

// https://leetcode.com/problems/russian-doll-envelopes/



import scala.collection.mutable



object Solution {

  def maxEnvelopes(envelopes: Array[Array[Int]]): Int = {

    val sorted = envelopes.sortWith { (left, right) =>

      if (left(0) != right(0)) {

        left(0) < right(0)

      } else {

        right(1) < left(1)

      }

    }



    val tails = mutable.ArrayBuffer.empty[Int]

    for (envelope <- sorted) {

      val height = envelope(1)

      val index = lowerBound(tails, height)

      if (index == tails.size) {

        tails += height

      } else {

        tails(index) = height

      }

    }



    tails.size

  }



  private def lowerBound(values: mutable.ArrayBuffer[Int], target: Int): Int = {

    var left = 0

    var right = values.size

    while (left < right) {

      val mid = left + (right - left) / 2

      if (values(mid) < target) {

        left = mid + 1

      } else {

        right = mid

      }

    }

    left

  }

}
