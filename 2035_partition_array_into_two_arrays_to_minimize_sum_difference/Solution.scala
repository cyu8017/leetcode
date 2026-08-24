// LeetCode 2035 - Partition Array Into Two Arrays to Minimize Sum Difference
// https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/

object Solution {
  def minimumDifference(nums: Array[Int]): Int = {
    val n = nums.length / 2
    var total = 0
    nums.foreach { v => total += v }
    val left = nums.slice(0, n)
    val right = nums.slice(n, nums.length)
    def sumsByCount(arr: Array[Int]): Array[Array[Int]] = {
      val m = arr.length
      val res = Array.fill(m + 1)(scala.collection.mutable.ArrayBuffer.empty[Int])
      var mask = 0
      while (mask < (1 << m)) {
        var sum = 0
        var c = 0
        var i = 0
        while (i < m) {
          if ((mask & (1 << i)) != 0) { sum += arr(i); c += 1 }
          i += 1
        }
        res(c) += sum
        mask += 1
      }
      res.map(_.sorted.toArray)
    }
    val L = sumsByCount(left)
    val R = sumsByCount(right)
    var ans = Int.MaxValue
    var k = 0
    while (k <= n) {
      val arr = R(n - k)
      L(k).foreach { s1 =>
        val need = total / 2 - s1
        var lo = 0
        var hi = arr.length
        while (lo < hi) {
          val mid = (lo + hi) / 2
          if (arr(mid) < need) lo = mid + 1
          else hi = mid
        }
        val idxs = Array(lo - 1, lo)
        idxs.foreach { j =>
          if (j >= 0 && j < arr.length) {
            val s2 = arr(j)
            ans = math.min(ans, math.abs(total - 2 * (s1 + s2)))
          }
        }
      }
      k += 1
    }
    ans
  }
}
