// LeetCode 2866 - Beautiful Towers II
// https://leetcode.com/problems/beautiful-towers-ii/

object Solution {
  def maximumSumOfHeights(maxHeights: Array[Int]): Long = {
    val n = maxHeights.length
    val left = Array.fill(n)(0L)
    val st = scala.collection.mutable.ArrayBuffer(-1)
    var sum = 0L
    for (i <- 0 until n) {
      while (st.length > 1 && maxHeights(st.last) >= maxHeights(i)) {
        val j = st.remove(st.length - 1)
        sum -= 1L * maxHeights(j) * (j - st.last)
      }
      sum += 1L * maxHeights(i) * (i - st.last)
      left(i) = sum
      st += i
    }
    val right = Array.fill(n)(0L)
    st.clear()
    st += n
    sum = 0
    for (i <- n - 1 to 0 by -1) {
      while (st.length > 1 && maxHeights(st.last) >= maxHeights(i)) {
        val j = st.remove(st.length - 1)
        sum -= 1L * maxHeights(j) * (st.last - j)
      }
      sum += 1L * maxHeights(i) * (st.last - i)
      right(i) = sum
      st += i
    }
    var ans = 0L
    for (i <- 0 until n) {
      val cand = left(i) + right(i) - maxHeights(i)
      if (cand > ans) ans = cand
    }
    ans
  }
}
