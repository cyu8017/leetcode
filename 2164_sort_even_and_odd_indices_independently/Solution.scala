// LeetCode 2164 - Sort Even and Odd Indices Independently
// https://leetcode.com/problems/sort-even-and-odd-indices-independently/

object Solution {
  def sortEvenOdd(nums: Array[Int]): Array[Int] = {
    val even = scala.collection.mutable.ArrayBuffer.empty[Int]
    val odd = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < nums.length) {
      if (i % 2 == 0) even += nums(i)
      else odd += nums(i)
      i += 1
    }
    val es = even.sorted
    val os = odd.sorted(Ordering[Int].reverse)
    var ei = 0
    var oi = 0
    i = 0
    while (i < nums.length) {
      if (i % 2 == 0) { nums(i) = es(ei); ei += 1 }
      else { nums(i) = os(oi); oi += 1 }
      i += 1
    }
    nums
  }
}
