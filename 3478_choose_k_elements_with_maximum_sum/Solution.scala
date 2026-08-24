// LeetCode 3478 - Choose K Elements With Maximum Sum
// https://leetcode.com/problems/choose-k-elements-with-maximum-sum/

object Solution {
  def findMaxSum(nums1: Array[Int], nums2: Array[Int], k: Int): Array[Long] = {
    val n = nums1.length
    val arr = Array.tabulate(n)(i => Array(nums1(i), nums2(i), i))
    java.util.Arrays.sort(arr, (a: Array[Int], b: Array[Int]) => java.lang.Integer.compare(a(0), b(0)))
    val ans = new Array[Long](n)
    val h = new java.util.PriorityQueue[Integer]()
    var sum = 0L
    var i = 0
    while (i < n) {
      val v = arr(i)(0)
      val start = i
      while (i < n && arr(i)(0) == v) i += 1
      var t = start
      while (t < i) { ans(arr(t)(2)) = sum; t += 1 }
      t = start
      while (t < i) {
        h.offer(arr(t)(1))
        sum += arr(t)(1)
        if (h.size() > k) sum -= h.poll()
        t += 1
      }
    }
    ans
  }
}
