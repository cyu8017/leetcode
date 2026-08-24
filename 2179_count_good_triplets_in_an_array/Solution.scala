// LeetCode 2179 - Count Good Triplets in an Array
// https://leetcode.com/problems/count-good-triplets-in-an-array/

object Solution {
  private class Fenwick(n: Int) {
    private val bit = Array.fill(n)(0)
    def add(i0: Int, v: Int): Unit = {
      var i = i0
      while (i < bit.length) {
        bit(i) += v
        i += i & -i
      }
    }
    def sum(i0: Int): Int = {
      var i = i0
      var s = 0
      while (i > 0) {
        s += bit(i)
        i -= i & -i
      }
      s
    }
  }

  def goodTriplets(nums1: Array[Int], nums2: Array[Int]): Long = {
    val n = nums1.length
    val pos2 = Array.fill(n)(0)
    val mapped = Array.fill(n)(0)
    val left = Array.fill(n)(0)
    val right = Array.fill(n)(0)
    var i = 0
    while (i < n) {
      pos2(nums2(i)) = i
      i += 1
    }
    i = 0
    while (i < n) {
      mapped(i) = pos2(nums1(i))
      i += 1
    }
    var fw = new Fenwick(n + 2)
    i = 0
    while (i < n) {
      left(i) = fw.sum(mapped(i))
      fw.add(mapped(i) + 1, 1)
      i += 1
    }
    fw = new Fenwick(n + 2)
    i = n - 1
    while (i >= 0) {
      right(i) = fw.sum(n) - fw.sum(mapped(i) + 1)
      fw.add(mapped(i) + 1, 1)
      i -= 1
    }
    var ans = 0L
    i = 0
    while (i < n) {
      ans += 1L * left(i) * right(i)
      i += 1
    }
    ans
  }
}
