// LeetCode 1868 - Product of Two Run-Length Encoded Arrays
// https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/

import scala.collection.mutable

object Solution {
  def findRLEArray(encoded1: Array[Array[Int]], encoded2: Array[Array[Int]]): Array[Array[Int]] = {
    val result = mutable.ArrayBuffer.empty[Array[Int]]
    var i = 0
    var j = 0
    var rem1 = encoded1(0)(1)
    var rem2 = encoded2(0)(1)

    while (i < encoded1.length) {
      val take = math.min(rem1, rem2)
      val value = encoded1(i)(0) * encoded2(j)(0)
      if (result.nonEmpty && result.last(0) == value) {
        result.last(1) += take
      } else {
        result += Array(value, take)
      }
      rem1 -= take
      rem2 -= take
      if (rem1 == 0) {
        i += 1
        if (i < encoded1.length) rem1 = encoded1(i)(1)
      }
      if (rem2 == 0) {
        j += 1
        if (j < encoded2.length) rem2 = encoded2(j)(1)
      }
    }
    result.toArray
  }
}
