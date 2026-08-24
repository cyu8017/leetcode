// LeetCode 0949 - Largest Time for Given Digits
// https://leetcode.com/problems/largest-time-for-given-digits/

object Solution {
  def largestTimeFromDigits(arr: Array[Int]): String = {
    scala.util.Sorting.quickSort(arr)
    var best = ""
    def nextPermutation(a: Array[Int]): Boolean = {
      var i = a.length - 2
      while (i >= 0 && a(i) >= a(i + 1)) i -= 1
      if (i < 0) return false
      var j = a.length - 1
      while (a(j) <= a(i)) j -= 1
      val tmp = a(i); a(i) = a(j); a(j) = tmp
      var l = i + 1
      var r = a.length - 1
      while (l < r) {
        val t = a(l); a(l) = a(r); a(r) = t
        l += 1; r -= 1
      }
      true
    }
    do {
      val hours = 10 * arr(0) + arr(1)
      val minutes = 10 * arr(2) + arr(3)
      if (hours < 24 && minutes < 60) {
        val cand = f"${hours}%02d:${minutes}%02d"
        if (cand > best) best = cand
      }
    } while (nextPermutation(arr))
    best
  }
}
