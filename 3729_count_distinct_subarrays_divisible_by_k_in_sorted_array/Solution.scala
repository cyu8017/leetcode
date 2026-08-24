// LeetCode 3729 - Count Distinct Subarrays Divisible By K In Sorted Array
// https://leetcode.com/problems/count-distinct-subarrays-divisible-by-k-in-sorted-array/

object Solution {
  def numGoodSubarrays(nums: Array[Int], k: Int): Long = {
    var ans = 0L
    var s = 0
    val cnt = new java.util.HashMap[Integer, Integer]()
    cnt.put(0, 1)
    nums.foreach { x =>
      s = (s + x) % k
      ans += cnt.getOrDefault(s, 0)
      cnt.merge(s, 1, (a: Integer, b: Integer) => Integer.valueOf(a + b))
    }
    val n = nums.length
    var i = 0
    while (i < n) {
      var j = i + 1
      while (j < n && nums(j) == nums(i)) j += 1
      val m = j - i
      var h = 1
      while (h <= m) {
        if (1L * nums(i) * h % k == 0) ans -= (m - h)
        h += 1
      }
      i = j
    }
    ans
  }
}
