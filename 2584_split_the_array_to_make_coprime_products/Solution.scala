// LeetCode 2584 - Split the Array to Make Coprime Products
// https://leetcode.com/problems/split-the-array-to-make-coprime-products/

object Solution {
  def findValidSplit(nums: Array[Int]): Int = {
    val first = scala.collection.mutable.Map.empty[Int, Int]
    val last = scala.collection.mutable.Map.empty[Int, Int]
    def factorize(x0: Int, idx: Int): Unit = {
      var x = x0
      var p = 2
      while (p.toLong * p <= x) {
        if (x % p == 0) {
          if (!first.contains(p)) first(p) = idx
          last(p) = idx
          while (x % p == 0) x /= p
        }
        p += 1
      }
      if (x > 1) {
        if (!first.contains(x)) first(x) = idx
        last(x) = idx
      }
    }
    val n = nums.length
    var i = 0
    while (i < n) {
      factorize(nums(i), i)
      i += 1
    }
    var far = 0
    i = 0
    while (i < n - 1) {
      var x = nums(i)
      var p = 2
      while (p.toLong * p <= x) {
        if (x % p == 0) {
          if (last(p) > far) far = last(p)
          while (x % p == 0) x /= p
        }
        p += 1
      }
      if (x > 1 && last(x) > far) far = last(x)
      if (far == i) return i
      i += 1
    }
    -1
  }
}
