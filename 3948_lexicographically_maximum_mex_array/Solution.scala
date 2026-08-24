// LeetCode 3948 - Lexicographically Maximum MEX Array
// https://leetcode.com/problems/lexicographically-maximum-mex-array/

import scala.collection.mutable

object Solution {
  def maxMexArray(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val remaining = new Array[Int](n + 2)
    for (x <- nums) {
      if (x <= n + 1) remaining(x) += 1
    }
    var mex = 0
    while (remaining(mex) > 0) mex += 1
    val answer = mutable.ArrayBuffer.empty[Int]
    val seen = new Array[Int](n + 2)
    var stamp = 0
    var index = 0
    while (index < n) {
      if (mex == 0) {
        answer += 0
        val x = nums(index)
        if (x <= n + 1) remaining(x) -= 1
        index += 1
      } else {
        stamp += 1
        var need = mex
        while (need > 0) {
          val x = nums(index)
          if (x < mex && seen(x) != stamp) {
            seen(x) = stamp
            need -= 1
          }
          if (x <= n + 1) remaining(x) -= 1
          index += 1
        }
        answer += mex
        mex = 0
        while (remaining(mex) > 0) mex += 1
      }
    }
    answer.toArray
  }
}
