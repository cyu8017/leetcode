// LeetCode 3943 - Number of Pairs After Increment
// https://leetcode.com/problems/number-of-pairs-after-increment/

import scala.collection.mutable

object Solution {
  def numberOfPairs(nums1: Array[Int], nums2: Array[Int], queries: Array[Array[Int]]): Array[Long] = {
    val blockSize = 225
    val n = nums2.length
    val blocks = (n + blockSize - 1) / blockSize
    val pending = new Array[Int](blocks)
    val freq = Array.fill(blocks)(mutable.HashMap.empty[Int, Int])
    var b = 0
    while (b < blocks) {
      rebuild(freq, nums2, b, blockSize, n)
      b += 1
    }
    val fixed = mutable.HashMap.empty[Int, Int]
    for (x <- nums1) fixed(x) = fixed.getOrElse(x, 0) + 1
    val answer = mutable.ArrayBuffer.empty[Long]
    for (q <- queries) {
      if (q(0) == 1) {
        val l = q(1)
        val r = q(2)
        val delta = q(3)
        val first = l / blockSize
        val last = r / blockSize
        if (first == last) {
          push(pending, nums2, first, blockSize, n)
          var i = l
          while (i <= r) {
            nums2(i) += delta
            i += 1
          }
          rebuild(freq, nums2, first, blockSize, n)
        } else {
          push(pending, nums2, first, blockSize, n)
          var i = l
          while (i < (first + 1) * blockSize) {
            nums2(i) += delta
            i += 1
          }
          rebuild(freq, nums2, first, blockSize, n)
          push(pending, nums2, last, blockSize, n)
          i = last * blockSize
          while (i <= r) {
            nums2(i) += delta
            i += 1
          }
          rebuild(freq, nums2, last, blockSize, n)
          b = first + 1
          while (b < last) {
            pending(b) += delta
            b += 1
          }
        }
      } else {
        var total = 0L
        for ((a, countA) <- fixed) {
          val target = q(1) - a
          b = 0
          while (b < blocks) {
            freq(b).get(target - pending(b)).foreach { c =>
              total += countA.toLong * c
            }
            b += 1
          }
        }
        answer += total
      }
    }
    answer.toArray
  }

  private def rebuild(
      freq: Array[mutable.HashMap[Int, Int]],
      nums2: Array[Int],
      b: Int,
      blockSize: Int,
      n: Int
  ): Unit = {
    freq(b).clear()
    val end = math.min((b + 1) * blockSize, n)
    var i = b * blockSize
    while (i < end) {
      freq(b)(nums2(i)) = freq(b).getOrElse(nums2(i), 0) + 1
      i += 1
    }
  }

  private def push(pending: Array[Int], nums2: Array[Int], b: Int, blockSize: Int, n: Int): Unit = {
    if (pending(b) != 0) {
      val end = math.min((b + 1) * blockSize, n)
      var i = b * blockSize
      while (i < end) {
        nums2(i) += pending(b)
        i += 1
      }
      pending(b) = 0
    }
  }
}
