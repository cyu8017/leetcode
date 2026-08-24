// LeetCode 3321 - Find X-Sum of All K-Long Subarrays II
// https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/

object Solution {
  def findXSum(nums: Array[Int], k: Int, x: Int): Array[Long] = {
    val n = nums.length
    val ans = new Array[Long](n - k + 1)
    var i = 0
    while (i <= n - k) {
      val freq = scala.collection.mutable.HashMap.empty[Int, Int]
      var j = i
      while (j < i + k) {
        freq(nums(j)) = freq.getOrElse(nums(j), 0) + 1
        j += 1
      }
      val arr = freq.toArray
      var a = 0
      while (a < arr.length) {
        var b = a + 1
        while (b < arr.length) {
          val A = arr(a)
          val B = arr(b)
          if (B._2 > A._2 || (B._2 == A._2 && B._1 > A._1)) {
            arr(a) = B
            arr(b) = A
          }
          b += 1
        }
        a += 1
      }
      val lim = math.min(x, arr.length)
      val keep = scala.collection.mutable.HashSet.empty[Int]
      var t = 0
      while (t < lim) {
        keep += arr(t)._1
        t += 1
      }
      var sum = 0L
      j = i
      while (j < i + k) {
        if (keep.contains(nums(j))) sum += nums(j)
        j += 1
      }
      ans(i) = sum
      i += 1
    }
    ans
  }
}
